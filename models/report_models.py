from abc import ABC, abstractmethod
from datetime import datetime

class SystemReport(ABC):
    @abstractmethod
    def generate(self, lms_obj):
        pass

class UserReport(SystemReport):
    def generate(self, lms_obj):
        report = f"USER AUDIT REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        report += "="*50 + "\n"
        report += f"{'Role':<12} | {'Username':<15} | {'Email'}\n"
        report += "-"*50 + "\n"
        for u in lms_obj.users:
            report += f"{u.get_role():<12} | {u.get_username():<15} | {u.get_email()}\n"
        return report

class CourseReport(SystemReport):
    def generate(self, lms_obj):
        report = f"COURSE PERFORMANCE REPORT\n"
        report += "="*50 + "\n"
        for c in lms_obj.courses:
            reviews = c.reviews
            if reviews:
                 avg_rating = sum(r._CourseReview__rating for r in reviews) / len(reviews)
            else:
                avg_rating = 0
                
            report += f"Course: {c.title} (Rating: {avg_rating:.1f}/5.0)\n"
            report += f"Students: {len(c.students)} | Reviews: {len(c.reviews)}\n"
            report += "-"*50 + "\n"
        return report

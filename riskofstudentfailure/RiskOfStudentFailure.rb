# RiskOfStudentFailure.rb
class RiskOfStudentFailure
  def self.check_for_failure(student_engagement, threshold)
    if student_engagement >= threshold
      "Student is not at risk"
    elsif student_engagement < threshold
      "Student is at risk"
    end
  end
end


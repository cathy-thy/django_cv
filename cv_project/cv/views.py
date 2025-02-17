from django.shortcuts import render

def cv_view(request):
    from django.shortcuts import render

def cv_view(request):
    cv_data = {
        'name': 'Ho-Yan (Cathy) Tsui',
        'linkedin': 'https://www.linkedin.com/in/cathy-tsui',
        'github': 'https://github.com/cathy-thy',
        'education': [
            {
                'degree': 'M.S. in Computer Science',
                'institution': 'New York University',
                'location': 'New York',
                'dates': '09/2024 – Present',
                'courses': [
                    'Artificial Intelligence', 'Data Science',
                    'Discrete Mathematics', 'Design & Analysis of Algorithms'
                ]
            },
            {
                'degree': 'B.B.A in Professional Accountancy, Minor in Computer Science (First Class Honors)',
                'institution': 'The Chinese University of Hong Kong',
                'location': 'Hong Kong',
                'dates': '09/2015 – 07/2020'
            }
        ],
        'experience': [
            {
                'role': 'Business Intelligence Engineer, Digital, Data & AI',
                'company': 'Jardine Matheson Holdings Limited',
                'location': 'Hong Kong',
                'dates': '01/2023 – 08/2024',
                'responsibilities': [
                    'Developed a data pipeline using PySpark within Databricks for 8 million IKEA users.',
                    'Designed a partitioning and caching strategy to improve data efficiency by 25%.',
                    'Implemented machine learning models to predict financial performance with 20% improved accuracy.'
                ]
            },
            {
                'role': 'Consultant, Insights and Data',
                'company': 'Capgemini Hong Kong Limited',
                'location': 'Hong Kong',
                'dates': '03/2021 – 12/2022',
                'responsibilities': [
                    'Designed a data warehouse using Data Vault 2.0 for an international insurance company.',
                    'Automated over 20 financial reports using Power BI, reducing report preparation time by 80%.'
                ]
            }
        ],
        'skills': [
            'Python', 'Django', 'PySpark', 'SQL', 'JavaScript', 'HTML', 'CSS',
            'Databricks', 'Snowflake', 'AWS', 'Azure', 'GCP', 'DevOps'
        ],
        'certifications': [
            'AWS Solutions Architect',
            'GCP Professional Data Engineer',
            'Azure Power BI Data Analyst Associate'
        ],
        'projects': [
            {
                'name': 'Spotify Music Recommendation System',
                'description': 'Developed a recommendation model using KNN & SVM for personalized song suggestions.'
            },
            {
                'name': 'Customer Purchase Behavior Analysis',
                'description': 'Analyzed retail customer data using multiple regression with PyMC and MCMC techniques.'
            }
        ]
    }

    return render(request, 'cv_template.html', {'cv': cv_data})

# Create your views here.

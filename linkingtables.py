from hackkings import db

developer_project_link = db.Table('user_project_link',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

skill_projects_link = db.Table('skill_project_link',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

skill_users_link = db.Table('skill_user_link',
    db.Column('skill_id', db.Integer, db.ForeignKey('skill.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

thread_link = db.Table('members', 
    db.Column('thread_id', db.Integer, db.ForeignKey('message_thread.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)
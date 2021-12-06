%define        gemname rails

Name:          gem-rails
Version:       6.1.4.1
Release:       alt2
Summary:       Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://rubyonrails.org/
Vcs:           https://github.com/rails/rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       railsctl
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(i18n) >= 1.6 gem(i18n) < 2
BuildRequires: gem(tzinfo) >= 2.0 gem(tzinfo) < 3
BuildRequires: gem(concurrent-ruby) >= 1.0.2 gem(concurrent-ruby) < 2
BuildRequires: gem(zeitwerk) >= 2.3 gem(zeitwerk) < 3
BuildRequires: gem(minitest) >= 5.1 gem(minitest) < 6
BuildRequires: gem(nokogiri) >= 1.8.5
BuildRequires: gem(rack) >= 2.0 gem(rack) < 3
BuildRequires: gem(rack-test) >= 0.6.3
BuildRequires: gem(rails-html-sanitizer) >= 1.2.0 gem(rails-html-sanitizer) < 2
BuildRequires: gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
BuildRequires: gem(mail) >= 2.5.4 gem(mail) < 3
BuildRequires: gem(globalid) >= 0.3.6
BuildRequires: gem(rake) >= 0.13 gem(rake) < 14
BuildRequires: gem(thor) >= 1.0 gem(thor) < 2
BuildRequires: gem(method_source) >= 0
BuildRequires: gem(builder) >= 3.1 gem(builder) < 4
BuildRequires: gem(erubi) >= 1.4 gem(erubi) < 2
BuildRequires: gem(marcel) >= 1.0.0 gem(marcel) < 1.1
BuildRequires: gem(mini_mime) >= 1.1.0
BuildRequires: gem(bundler) >= 1.15.0 gem(bundler) < 3
#BuildRequires: gem(sprockets-rails) >= 3.2.2
BuildRequires: gem(mail) >= 2.7.1
BuildRequires: gem(nio4r) >= 2.0 gem(nio4r) < 3
BuildRequires: gem(websocket-driver) >= 0.6.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(actionview) = 6.1.4.1
Requires:      gem(activemodel) = 6.1.4.1
Requires:      gem(activerecord) = 6.1.4.1
Requires:      gem(actionmailer) = 6.1.4.1
Requires:      gem(activejob) = 6.1.4.1
Requires:      gem(actioncable) = 6.1.4.1
Requires:      gem(activestorage) = 6.1.4.1
Requires:      gem(actionmailbox) = 6.1.4.1
Requires:      gem(actiontext) = 6.1.4.1
Requires:      gem(railties) = 6.1.4.1
Requires:      gem(bundler) >= 1.15.0 gem(bundler) < 3
Requires:      gem(sprockets-rails) >= 2.0.0
Requires:      rails = %EVR
Obsoletes:     ruby-rails < %EVR
Provides:      ruby-rails = %EVR
Provides:      gem(rails) = 6.1.4.1


%description
Ruby on Rails metapackage gem.


%package       -n gem-activesupport
Version:       6.1.4.1
Release:       alt2
Summary:       A toolkit of support libraries and Ruby core extensions extracted from the Rails framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(i18n) >= 1.6 gem(i18n) < 2
Requires:      gem(tzinfo) >= 2.0 gem(tzinfo) < 3
Requires:      gem(concurrent-ruby) >= 1.0.2 gem(concurrent-ruby) < 2
Requires:      gem(zeitwerk) >= 2.3 gem(zeitwerk) < 3
Requires:      gem(minitest) >= 5.1 gem(minitest) < 6
Obsoletes:     activesupport-gems < %EVR
Obsoletes:     ruby-activesupport < %EVR
Provides:      activesupport-gems = %EVR
Provides:      ruby-activesupport = %EVR
Provides:      gem(activesupport) = 6.1.4.1

%description   -n gem-activesupport
A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.


%package       -n gem-activesupport-doc
Version:       6.1.4.1
Release:       alt2
Summary:       A toolkit of support libraries and Ruby core extensions extracted from the Rails framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activesupport
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Obsoletes:     ruby-activesupport-doc
Provides:      ruby-activesupport-doc

%description   -n gem-activesupport-doc
A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework documentation files.

A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.

%description   -n gem-activesupport-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activesupport.


%package       -n gem-activesupport-devel
Version:       6.1.4.1
Release:       alt2
Summary:       A toolkit of support libraries and Ruby core extensions extracted from the Rails framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activesupport
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1

%description   -n gem-activesupport-devel
A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework development package.

A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.

%description   -n gem-activesupport-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activesupport.


%package       -n gem-actiontext
Version:       6.1.4.1
Release:       alt2
Summary:       Edit and display rich text in Rails applications
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(activerecord) = 6.1.4.1
Requires:      gem(activestorage) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(nokogiri) >= 1.8.5
Provides:      gem(actiontext) = 6.1.4.1

%description   -n gem-actiontext
Action Text brings rich text content and editing to Rails. It includes the Trix
editor that handles everything from formatting to links to quotes to lists to
embedded images and galleries. The rich text content generated by the Trix
editor is saved in its own RichText model that's associated with any existing
Active Record model in the application. Any embedded images (or other
attachments) are automatically stored using Active Storage and associated with
the included RichText model.


%package       -n gem-actiontext-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Edit and display rich text in Rails applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actiontext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actiontext) = 6.1.4.1

%description   -n gem-actiontext-doc
Edit and display rich text in Rails applications documentation files.

Action Text brings rich text content and editing to Rails. It includes the Trix
editor that handles everything from formatting to links to quotes to lists to
embedded images and galleries. The rich text content generated by the Trix
editor is saved in its own RichText model that's associated with any existing
Active Record model in the application. Any embedded images (or other
attachments) are automatically stored using Active Storage and associated with
the included RichText model.

%description   -n gem-actiontext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actiontext.


%package       -n gem-actiontext-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Edit and display rich text in Rails applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actiontext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actiontext) = 6.1.4.1

%description   -n gem-actiontext-devel
Edit and display rich text in Rails applications development package.

Action Text brings rich text content and editing to Rails. It includes the Trix
editor that handles everything from formatting to links to quotes to lists to
embedded images and galleries. The rich text content generated by the Trix
editor is saved in its own RichText model that's associated with any existing
Active Record model in the application. Any embedded images (or other
attachments) are automatically stored using Active Storage and associated with
the included RichText model.

%description   -n gem-actiontext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actiontext.


%package       -n gem-actionpack
Version:       6.1.4.1
Release:       alt2
Summary:       Web-flow and rendering framework putting the VC in MVC (part of Rails)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(rack) >= 2.0 gem(rack) < 3
Requires:      gem(rack-test) >= 0.6.3 gem(rack-test) < 2
Requires:      gem(rails-html-sanitizer) >= 1.2.0 gem(rails-html-sanitizer) < 2
Requires:      gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
Requires:      gem(actionview) = 6.1.4.1
Obsoletes:     ruby-actionpack
Provides:      ruby-actionpack
Provides:      gem(actionpack) = 6.1.4.1

%description   -n gem-actionpack
Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.


%package       -n gem-actionpack-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Web-flow and rendering framework putting the VC in MVC (part of Rails) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionpack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionpack) = 6.1.4.1
Obsoletes:     ruby-actionpack-doc
Provides:      ruby-actionpack-doc

%description   -n gem-actionpack-doc
Web-flow and rendering framework putting the VC in MVC (part of Rails)
documentation files.

Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.

%description   -n gem-actionpack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionpack.


%package       -n gem-actionpack-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Web-flow and rendering framework putting the VC in MVC (part of Rails) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionpack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(activemodel) = 6.1.4.1

%description   -n gem-actionpack-devel
Web-flow and rendering framework putting the VC in MVC (part of Rails)
development package.

Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.

%description   -n gem-actionpack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionpack.


%package       -n gem-activemodel
Version:       6.1.4.1
Release:       alt2
Summary:       A toolkit for building modeling frameworks (part of Rails)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Obsoletes:     ruby-activemodel
Provides:      ruby-activemodel
Provides:      gem(activemodel) = 6.1.4.1

%description   -n gem-activemodel
A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.


%package       -n gem-activemodel-doc
Version:       6.1.4.1
Release:       alt2
Summary:       A toolkit for building modeling frameworks (part of Rails) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activemodel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activemodel) = 6.1.4.1
Obsoletes:     ruby-activemodel-doc
Provides:      ruby-activemodel-doc

%description   -n gem-activemodel-doc
A toolkit for building modeling frameworks (part of Rails) documentation
files.

A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.

%description   -n gem-activemodel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activemodel.


%package       -n gem-activemodel-devel
Version:       6.1.4.1
Release:       alt2
Summary:       A toolkit for building modeling frameworks (part of Rails) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activemodel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activemodel) = 6.1.4.1

%description   -n gem-activemodel-devel
A toolkit for building modeling frameworks (part of Rails) development
package.

A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.

%description   -n gem-activemodel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activemodel.


%package       -n gem-actionmailer
Version:       6.1.4.1
Release:       alt2
Summary:       Email composition, delivery, and receiving framework (part of Rails)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(actionview) = 6.1.4.1
Requires:      gem(activejob) = 6.1.4.1
Requires:      gem(mail) >= 2.5.4 gem(mail) < 3
Requires:      gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
Obsoletes:     ruby-actionmailer
Provides:      ruby-actionmailer
Provides:      gem(actionmailer) = 6.1.4.1

%description   -n gem-actionmailer
Email on Rails. Compose, deliver, receive, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.


%package       -n gem-actionmailer-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Email composition, delivery, and receiving framework (part of Rails) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionmailer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionmailer) = 6.1.4.1
Obsoletes:     ruby-actionmailer-doc
Provides:      ruby-actionmailer-doc

%description   -n gem-actionmailer-doc
Email composition, delivery, and receiving framework (part of Rails)
documentation files.

Email on Rails. Compose, deliver, receive, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%description   -n gem-actionmailer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionmailer.


%package       -n gem-actionmailer-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Email composition, delivery, and receiving framework (part of Rails) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionmailer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionmailer) = 6.1.4.1

%description   -n gem-actionmailer-devel
Email composition, delivery, and receiving framework (part of Rails) development
package.

Email on Rails. Compose, deliver, receive, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%description   -n gem-actionmailer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionmailer.


%package       -n gem-activerecord
Version:       6.1.4.1
Release:       alt2
Summary:       Object-relational mapper framework (part of Rails)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(activemodel) = 6.1.4.1
Obsoletes:     activerecord-gems < %EVR
Obsoletes:     ruby-activerecord < %EVR
Provides:      activerecord-gems = %EVR
Provides:      ruby-activerecord = %EVR
Provides:      gem(activerecord) = 6.1.4.1

%description   -n gem-activerecord
Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.


%package       -n gem-activerecord-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Object-relational mapper framework (part of Rails) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord) = 6.1.4.1

%description   -n gem-activerecord-doc
Object-relational mapper framework (part of Rails) documentation
files.

Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.

%description   -n gem-activerecord-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord.


%package       -n gem-activerecord-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Object-relational mapper framework (part of Rails) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord) = 6.1.4.1

%description   -n gem-activerecord-devel
Object-relational mapper framework (part of Rails) development
package.

Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.

%description   -n gem-activerecord-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord.


%package       -n gem-activejob
Version:       6.1.4.1
Release:       alt2
Summary:       Job framework with pluggable queues
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(globalid) >= 0.3.6
Obsoletes:     ruby-activejob < %EVR
Provides:      ruby-activejob = %EVR
Provides:      gem(activejob) = 6.1.4.1

%description   -n gem-activejob
Declare job classes that can be run by a variety of queueing backends.


%package       -n gem-activejob-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Job framework with pluggable queues documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activejob
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activejob) = 6.1.4.1

%description   -n gem-activejob-doc
Job framework with pluggable queues documentation files.

Declare job classes that can be run by a variety of queueing backends.

%description   -n gem-activejob-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activejob.


%package       -n gem-activejob-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Job framework with pluggable queues development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activejob
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activejob) = 6.1.4.1

%description   -n gem-activejob-devel
Job framework with pluggable queues development package.

Declare job classes that can be run by a variety of queueing backends.

%description   -n gem-activejob-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activejob.


%package       -n gem-railties
Version:       6.1.4.1
Release:       alt2
Summary:       Tools for creating, working with, and running Rails applications
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(rake) >= 0.13 gem(rake) < 14
Requires:      gem(thor) >= 1.0 gem(thor) < 2
Requires:      gem(method_source) >= 0
Obsoletes:     ruby-railties < %EVR
Provides:      ruby-railties = %EVR
Provides:      gem(railties) = 6.1.4.1

%description   -n gem-railties
Rails internals: application bootup, plugins, generators, and rake tasks.


%package       -n rails
Version:       6.1.4.1
Release:       alt2
Summary:       Tools for creating, working with, and running Rails applications executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета railties
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(railties) = 6.1.4.1

%description   -n rails
Tools for creating, working with, and running Rails applications
executable(s).

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n rails -l ru_RU.UTF-8
Исполнямка для самоцвета railties.


%package       -n gem-railties-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Tools for creating, working with, and running Rails applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета railties
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(railties) = 6.1.4.1

%description   -n gem-railties-doc
Tools for creating, working with, and running Rails applications documentation
files.

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n gem-railties-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета railties.


%package       -n gem-railties-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Tools for creating, working with, and running Rails applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета railties
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(railties) = 6.1.4.1
Requires:      gem(actionview) = 6.1.4.1

%description   -n gem-railties-devel
Tools for creating, working with, and running Rails applications development
package.

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n gem-railties-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета railties.


%package       -n gem-actionview
Version:       6.1.4.1
Release:       alt2
Summary:       Rendering framework putting the V in MVC (part of Rails)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(builder) >= 3.1 gem(builder) < 4
Requires:      gem(erubi) >= 1.4 gem(erubi) < 2
Requires:      gem(rails-html-sanitizer) >= 1.2.0 gem(rails-html-sanitizer) < 2
Requires:      gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
Obsoletes:     ruby-actionview < %EVR
Provides:      ruby-actionview = %EVR
Provides:      gem(actionview) = 6.1.4.1

%description   -n gem-actionview
Simple, battle-tested conventions and helpers for building web pages.


%package       -n gem-actionview-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Rendering framework putting the V in MVC (part of Rails) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionview
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionview) = 6.1.4.1

%description   -n gem-actionview-doc
Rendering framework putting the V in MVC (part of Rails) documentation
files.

Simple, battle-tested conventions and helpers for building web pages.

%description   -n gem-actionview-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionview.


%package       -n gem-actionview-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Rendering framework putting the V in MVC (part of Rails) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionview
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionview) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(activemodel) = 6.1.4.1

%description   -n gem-actionview-devel
Rendering framework putting the V in MVC (part of Rails) development
package.

Simple, battle-tested conventions and helpers for building web pages.

%description   -n gem-actionview-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionview.


%package       -n gem-activestorage
Version:       6.1.4.1
Release:       alt2
Summary:       Local and cloud file storage framework
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(activejob) = 6.1.4.1
Requires:      gem(activerecord) = 6.1.4.1
Requires:      gem(marcel) >= 1.0.0 gem(marcel) < 1.1
Requires:      gem(mini_mime) >= 1.1.0
Obsoletes:     ruby-activestorage < %EVR
Provides:      ruby-activestorage = %EVR
Provides:      gem(activestorage) = 6.1.4.1

%description   -n gem-activestorage
Attach cloud and local files in Rails applications.


%package       -n gem-activestorage-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Local and cloud file storage framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activestorage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activestorage) = 6.1.4.1

%description   -n gem-activestorage-doc
Local and cloud file storage framework documentation files.

Attach cloud and local files in Rails applications.

%description   -n gem-activestorage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activestorage.


%package       -n gem-activestorage-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Local and cloud file storage framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activestorage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activestorage) = 6.1.4.1

%description   -n gem-activestorage-devel
Local and cloud file storage framework development package.

Attach cloud and local files in Rails applications.

%description   -n gem-activestorage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activestorage.


%package       -n gem-actionmailbox
Version:       6.1.4.1
Release:       alt2
Summary:       Receive and process incoming emails in Rails applications
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(activerecord) = 6.1.4.1
Requires:      gem(activestorage) = 6.1.4.1
Requires:      gem(activejob) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(mail) >= 2.7.1
Provides:      gem(actionmailbox) = 6.1.4.1

%description   -n gem-actionmailbox
Action Mailbox routes incoming emails to controller-like mailboxes for
processing in Rails. It ships with ingresses for Mailgun, Mandrill, Postmark,
and SendGrid. You can also handle inbound mails directly via the built-in Exim,
Postfix, and Qmail ingresses.

The inbound emails are turned into InboundEmail records using Active Record and
feature lifecycle tracking, storage of the original email on cloud storage via
Active Storage, and responsible data handling with on-by-default
incineration.

These inbound emails are routed asynchronously using Active Job to one or
several dedicated mailboxes, which are capable of interacting directly with the
rest of your domain model.


%package       -n gem-actionmailbox-doc
Version:       6.1.4.1
Release:       alt2
Summary:       Receive and process incoming emails in Rails applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionmailbox
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionmailbox) = 6.1.4.1

%description   -n gem-actionmailbox-doc
Receive and process incoming emails in Rails applications documentation
files.

Action Mailbox routes incoming emails to controller-like mailboxes for
processing in Rails. It ships with ingresses for Mailgun, Mandrill, Postmark,
and SendGrid. You can also handle inbound mails directly via the built-in Exim,
Postfix, and Qmail ingresses.

The inbound emails are turned into InboundEmail records using Active Record and
feature lifecycle tracking, storage of the original email on cloud storage via
Active Storage, and responsible data handling with on-by-default
incineration.

These inbound emails are routed asynchronously using Active Job to one or
several dedicated mailboxes, which are capable of interacting directly with the
rest of your domain model.

%description   -n gem-actionmailbox-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionmailbox.


%package       -n gem-actionmailbox-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Receive and process incoming emails in Rails applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionmailbox
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionmailbox) = 6.1.4.1

%description   -n gem-actionmailbox-devel
Receive and process incoming emails in Rails applications development
package.

Action Mailbox routes incoming emails to controller-like mailboxes for
processing in Rails. It ships with ingresses for Mailgun, Mandrill, Postmark,
and SendGrid. You can also handle inbound mails directly via the built-in Exim,
Postfix, and Qmail ingresses.

The inbound emails are turned into InboundEmail records using Active Record and
feature lifecycle tracking, storage of the original email on cloud storage via
Active Storage, and responsible data handling with on-by-default
incineration.

These inbound emails are routed asynchronously using Active Job to one or
several dedicated mailboxes, which are capable of interacting directly with the
rest of your domain model.

%description   -n gem-actionmailbox-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionmailbox.


%package       -n gem-actioncable
Version:       6.1.4.1
Release:       alt2
Summary:       WebSocket framework for Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.4.1
Requires:      gem(actionpack) = 6.1.4.1
Requires:      gem(nio4r) >= 2.0 gem(nio4r) < 3
Requires:      gem(websocket-driver) >= 0.6.1
Obsoletes:     ruby-actioncable < %EVR
Provides:      ruby-actioncable = %EVR
Provides:      gem(actioncable) = 6.1.4.1

%description   -n gem-actioncable
Structure many real-time application concerns into channels over a single
WebSocket connection.


%package       -n gem-actioncable-doc
Version:       6.1.4.1
Release:       alt2
Summary:       WebSocket framework for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actioncable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actioncable) = 6.1.4.1

%description   -n gem-actioncable-doc
WebSocket framework for Rails documentation files.

Structure many real-time application concerns into channels over a single
WebSocket connection.

%description   -n gem-actioncable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actioncable.


%package       -n gem-actioncable-devel
Version:       6.1.4.1
Release:       alt2
Summary:       WebSocket framework for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actioncable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actioncable) = 6.1.4.1

%description   -n gem-actioncable-devel
WebSocket framework for Rails development package.

Structure many real-time application concerns into channels over a single
WebSocket connection.

%description   -n gem-actioncable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actioncable.


%package       -n gem-rails-devel
Version:       6.1.4.1
Release:       alt2
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails) = 6.1.4.1

%description   -n gem-rails-devel
Ruby on Rails development package.

Ruby on Rails metapackage gem.

%description   -n gem-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
install -D -m 755 %SOURCE1 %buildroot%_sbindir/railsctl

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-activesupport
%doc README.md
%ruby_gemspecdir/activesupport-6.1.4.1.gemspec
%ruby_gemslibdir/activesupport-6.1.4.1

%files         -n gem-activesupport-doc
%doc README.md
%ruby_gemsdocdir/activesupport-6.1.4.1

%files         -n gem-activesupport-devel
%doc README.md

%files         -n gem-actiontext
%doc actiontext/README.md
%ruby_gemspecdir/actiontext-6.1.4.1.gemspec
%ruby_gemslibdir/actiontext-6.1.4.1

%files         -n gem-actiontext-doc
%doc actiontext/README.md
%ruby_gemsdocdir/actiontext-6.1.4.1

%files         -n gem-actiontext-devel
%doc actiontext/README.md

%files         -n gem-actionpack
%doc README.md
%ruby_gemspecdir/actionpack-6.1.4.1.gemspec
%ruby_gemslibdir/actionpack-6.1.4.1

%files         -n gem-actionpack-doc
%doc README.md
%ruby_gemsdocdir/actionpack-6.1.4.1

%files         -n gem-actionpack-devel
%doc README.md

%files         -n gem-activemodel
%doc README.md
%ruby_gemspecdir/activemodel-6.1.4.1.gemspec
%ruby_gemslibdir/activemodel-6.1.4.1

%files         -n gem-activemodel-doc
%doc README.md
%ruby_gemsdocdir/activemodel-6.1.4.1

%files         -n gem-activemodel-devel
%doc README.md

%files         -n gem-actionmailer
%doc README.md
%ruby_gemspecdir/actionmailer-6.1.4.1.gemspec
%ruby_gemslibdir/actionmailer-6.1.4.1

%files         -n gem-actionmailer-doc
%doc README.md
%ruby_gemsdocdir/actionmailer-6.1.4.1

%files         -n gem-actionmailer-devel
%doc README.md

%files         -n gem-activerecord
%doc README.md
%ruby_gemspecdir/activerecord-6.1.4.1.gemspec
%ruby_gemslibdir/activerecord-6.1.4.1

%files         -n gem-activerecord-doc
%doc README.md
%ruby_gemsdocdir/activerecord-6.1.4.1

%files         -n gem-activerecord-devel
%doc README.md

%files         -n gem-activejob
%doc activejob/README.md
%ruby_gemspecdir/activejob-6.1.4.1.gemspec
%ruby_gemslibdir/activejob-6.1.4.1

%files         -n gem-activejob-doc
%doc activejob/README.md
%ruby_gemsdocdir/activejob-6.1.4.1

%files         -n gem-activejob-devel
%doc activejob/README.md

%files         -n gem-railties
%doc README.md
%ruby_gemspecdir/railties-6.1.4.1.gemspec
%ruby_gemslibdir/railties-6.1.4.1

%files         -n rails
%doc README.md
%_bindir/rails
%_sbindir/railsctl

%files         -n gem-railties-doc
%doc README.md
%ruby_gemsdocdir/railties-6.1.4.1

%files         -n gem-railties-devel
%doc README.md

%files         -n gem-actionview
%doc README.md
%ruby_gemspecdir/actionview-6.1.4.1.gemspec
%ruby_gemslibdir/actionview-6.1.4.1

%files         -n gem-actionview-doc
%doc README.md
%ruby_gemsdocdir/actionview-6.1.4.1

%files         -n gem-actionview-devel
%doc README.md

%files         -n gem-activestorage
%doc activestorage/README.md
%ruby_gemspecdir/activestorage-6.1.4.1.gemspec
%ruby_gemslibdir/activestorage-6.1.4.1

%files         -n gem-activestorage-doc
%doc activestorage/README.md
%ruby_gemsdocdir/activestorage-6.1.4.1

%files         -n gem-activestorage-devel
%doc activestorage/README.md

%files         -n gem-actionmailbox
%doc actionmailbox/README.md
%ruby_gemspecdir/actionmailbox-6.1.4.1.gemspec
%ruby_gemslibdir/actionmailbox-6.1.4.1

%files         -n gem-actionmailbox-doc
%doc actionmailbox/README.md
%ruby_gemsdocdir/actionmailbox-6.1.4.1

%files         -n gem-actionmailbox-devel
%doc actionmailbox/README.md

%files         -n gem-actioncable
%doc actioncable/README.md
%ruby_gemspecdir/actioncable-6.1.4.1.gemspec
%ruby_gemslibdir/actioncable-6.1.4.1

%files         -n gem-actioncable-doc
%doc actioncable/README.md
%ruby_gemsdocdir/actioncable-6.1.4.1

%files         -n gem-actioncable-devel
%doc actioncable/README.md

%files         -n gem-rails-devel
%doc README.md


%changelog
* Tue Oct 26 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.4.1-alt2
- + application sysconfig variable stack as exports
- * railsctl:
 + + reconstruction public web tree if any
 + - disabling the wepback:compile and assers:precompile

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.4.1-alt1
- ^ 6.1.3.2 -> 6.1.4.1
- ! CVE-2021-22942, CVE-2021-22881
- ! spec

* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.3.2-alt1
- ^ 5.2.4.4 -> 6.1.3.2
- ! CVE-2020-8185, CVE-2020-8166, CVE-2020-8167, CVE-2021-22880, CVE-2021-22902
- ! spec

* Mon Feb 15 2021 Pavel Skrylev <majioa@altlinux.org> 5.2.4.4-alt2
- * refactoring railsctl conforming to rails foreman installation

* Mon Nov 30 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.4-alt1
- ^ 5.2.4.3 -> 5.2.4.4
- ! CVE-2020-15169
- * railsctl to support locale setup

* Mon Jun 29 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.3-alt1
- ^ 5.2.4.1 -> 5.2.4.3
- ! bugfixes
 + - CVE-2020-8162
 + - CVE-2020-8164
 + - CVE-2020-8165
 + - CVE-2020-8166
 + - CVE-2020-8167

* Tue May 19 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt4
- * railsctl tmp detection, minor fixes

* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt3
- + 'mrproper' procedure to railsctl
- ! railsctl 'setup' procedure

* Fri May 08 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt2
- ! railsctl

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.4.1-alt1
- ^ 5.2.3 -> 5.2.4.1
- + railsctl command script to control rails app setup
- ! spec tags

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.3-alt1.1
- fixed (!) spec to fix dependency

* Tue Apr 02 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.3-alt1
- Bump to 5.2.3

* Mon Mar 25 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.2.1-alt2
- Added join lib and bin for railties gem

* Thu Mar 14 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.2.1-alt1
- Bump to 5.2.2.1;
- fix CVE-2019-5418, CVE-2019-5420.

* Sat Mar 09 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.2-alt1
- Bump to 5.2.2;
- Use Ruby Policy 2.0.

* Wed Jan 23 2019 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1.2
- Remove deprecated macros.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- Initial build for Sisyphus

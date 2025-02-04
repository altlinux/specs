%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rails

Name:          gem-rails
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://rubyonrails.org/
Vcs:           https://github.com/rails/rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.15.0
BuildRequires: gem(racc) >= 1.4.6
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(aws-sdk-sns) >= 0
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bcrypt) >= 3.1.11
BuildRequires: gem(benchmark) >= 0.3
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(bootsnap) >= 1.4.4
BuildRequires: gem(brakeman) >= 0
BuildRequires: gem(builder) >= 3.1
BuildRequires: gem(capybara) >= 3.39
BuildRequires: gem(cgi) >= 0.3.6
BuildRequires: gem(concurrent-ruby) >= 1.0.2
BuildRequires: gem(connection_pool) >= 2.2.5
BuildRequires: gem(cssbundling-rails) >= 0
BuildRequires: gem(dalli) >= 3.0.1
BuildRequires: gem(dartsass-rails) >= 0
BuildRequires: gem(drb) >= 0
BuildRequires: gem(erubi) >= 1.11
BuildRequires: gem(globalid) >= 0.6.0
BuildRequires: gem(httpclient) >= 0
BuildRequires: gem(i18n) >= 1.6
BuildRequires: gem(importmap-rails) >= 1.2.3
BuildRequires: gem(irb) >= 0
BuildRequires: gem(jbuilder) >= 0
BuildRequires: gem(jsbundling-rails) >= 0
BuildRequires: gem(launchy) >= 0
BuildRequires: gem(libxml-ruby) >= 0
BuildRequires: gem(listen) >= 3.3
BuildRequires: gem(logger) >= 1.4.2
BuildRequires: gem(mail) >= 2.8.0
BuildRequires: gem(marcel) >= 1.0
BuildRequires: gem(minitest) >= 5.1
BuildRequires: gem(minitest-bisect) >= 0
BuildRequires: gem(minitest-ci) >= 0
BuildRequires: gem(minitest-retry) >= 0
BuildRequires: gem(msgpack) >= 1.7.0
BuildRequires: gem(mutex_m) >= 0
BuildRequires: gem(net-imap) >= 0
BuildRequires: gem(net-pop) >= 0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(nio4r) >= 2.0
BuildRequires: gem(nokogiri) >= 1.8.5
BuildRequires: gem(prism) >= 0
BuildRequires: gem(propshaft) >= 0.1.7
BuildRequires: gem(rack) >= 2.2.4
BuildRequires: gem(rack-cache) >= 1.2
BuildRequires: gem(rack-session) >= 1.0.1
BuildRequires: gem(rack-test) >= 0.6.3
BuildRequires: gem(rackup) >= 1.0.0
BuildRequires: gem(rails-dom-testing) >= 2.2
BuildRequires: gem(rails-html-sanitizer) >= 1.6
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(securerandom) >= 0.3
BuildRequires: gem(selenium-webdriver) >= 4.11.0
BuildRequires: gem(sprockets-rails) >= 2.0.0
BuildRequires: gem(sqlite3) >= 1.6.6
BuildRequires: gem(stimulus-rails) >= 0
BuildRequires: gem(syntax_tree) >= 6.1.1
BuildRequires: gem(tailwindcss-rails) >= 0
BuildRequires: gem(terser) >= 1.1.4
BuildRequires: gem(thor) >= 1.0
BuildRequires: gem(timeout) >= 0.4.0
BuildRequires: gem(turbo-rails) >= 0
BuildRequires: gem(tzinfo) >= 2.0.5
BuildRequires: gem(useragent) >= 0.16
BuildRequires: gem(web-console) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(websocket-driver) >= 0.6.1
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(bcrypt) >= 3.2
BuildConflicts: gem(builder) >= 4
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(erubi) >= 2
BuildConflicts: gem(i18n) >= 2
BuildConflicts: gem(importmap-rails) >= 2.0.2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(listen) >= 4
BuildConflicts: gem(mail) >= 3
BuildConflicts: gem(marcel) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(nio4r) >= 3
BuildConflicts: gem(nokogiri) >= 1.11.0
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rack-cache) >= 2
BuildConflicts: gem(rails-dom-testing) >= 3
BuildConflicts: gem(rails-html-sanitizer) >= 2
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(tzinfo) >= 3
BuildConflicts: gem(useragent) >= 1
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency redis >= 6.0.0,redis < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rack >= 3.1.7,rack < 4
%ruby_use_gem_dependency syntax_tree >= 6.2.0,syntax_tree < 7
Requires:      ruby >= 2.7.0
Requires:      rubygems >= 1.8.11
Requires:      gem(bundler) >= 1.15.0
Obsoletes:     ruby-rails < %EVR
Provides:      ruby-rails = %EVR
Provides:      gem(rails) = 7.1.5.1

%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


%package       -n gem-railties
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(irb) >= 0
Requires:      gem(rackup) >= 1.0.0
Requires:      gem(rake) >= 12.2
Requires:      gem(thor) >= 1.2.2
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(thor) >= 2
Conflicts:     gem(zeitwerk) >= 3
Provides:      railties = %EVR
Provides:      gem(railties) = 7.1.5.1

%description   -n gem-railties
Rails internals: application bootup, plugins, generators, and rake tasks.


%package       -n rails
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета railties
Group:         Other
BuildArch:     noarch

Requires:      gem(railties) = 7.1.5.1

%description   -n rails
Ruby on Rails executable(s).

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n rails -l ru_RU.UTF-8
Исполнямка для самоцвета railties.


%if_enabled    doc
%package       -n gem-railties-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета railties
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(railties) = 7.1.5.1

%description   -n gem-railties-doc
Ruby on Rails documentation files.

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n gem-railties-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета railties.
%endif


%if_enabled    devel
%package       -n gem-railties-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета railties
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(railties) = 7.1.5.1

%description   -n gem-railties-devel
Ruby on Rails development package.

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n gem-railties-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета railties.
%endif


%package       -n gem-activejob
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(globalid) >= 0.3.6
Provides:      activejob = %EVR
Provides:      gem(activejob) = 7.1.5.1

%description   -n gem-activejob
Declare job classes that can be run by a variety of queuing backends.


%if_enabled    doc
%package       -n gem-activejob-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activejob
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activejob) = 7.1.5.1

%description   -n gem-activejob-doc
Ruby on Rails documentation files.

Declare job classes that can be run by a variety of queuing backends.

%description   -n gem-activejob-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activejob.
%endif


%if_enabled    devel
%package       -n gem-activejob-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activejob
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activejob) = 7.1.5.1

%description   -n gem-activejob-devel
Ruby on Rails development package.

Declare job classes that can be run by a variety of queuing backends.

%description   -n gem-activejob-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activejob.
%endif


%package       -n gem-actionview
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(builder) >= 3.1
Requires:      gem(erubi) >= 1.11
Requires:      gem(rails-dom-testing) >= 2.2
Requires:      gem(rails-html-sanitizer) >= 1.6
Conflicts:     gem(builder) >= 4
Conflicts:     gem(erubi) >= 2
Conflicts:     gem(rails-dom-testing) >= 3
Conflicts:     gem(rails-html-sanitizer) >= 2
Provides:      actionview = %EVR
Provides:      gem(actionview) = 7.1.5.1

%description   -n gem-actionview
Simple, battle-tested conventions and helpers for building web pages.


%if_enabled    doc
%package       -n gem-actionview-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionview
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionview) = 7.1.5.1

%description   -n gem-actionview-doc
Ruby on Rails documentation files.

Simple, battle-tested conventions and helpers for building web pages.

%description   -n gem-actionview-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionview.
%endif


%if_enabled    devel
%package       -n gem-actionview-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionview
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionview) = 7.1.5.1

%description   -n gem-actionview-devel
Ruby on Rails development package.

Simple, battle-tested conventions and helpers for building web pages.

%description   -n gem-actionview-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionview.
%endif


%package       -n gem-actiontext
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) = 7.1.5.1
Requires:      gem(activerecord) = 7.1.5.1
Requires:      gem(activestorage) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(globalid) >= 0.6.0
Requires:      gem(nokogiri) >= 1.8.5
Provides:      actiontext = %EVR
Provides:      gem(actiontext) = 7.1.5.1

%description   -n gem-actiontext
Edit and display rich text in Rails applications.


%if_enabled    doc
%package       -n gem-actiontext-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actiontext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actiontext) = 7.1.5.1

%description   -n gem-actiontext-doc
Ruby on Rails documentation files.

Edit and display rich text in Rails applications.

%description   -n gem-actiontext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actiontext.
%endif


%if_enabled    devel
%package       -n gem-actiontext-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actiontext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actiontext) = 7.1.5.1

%description   -n gem-actiontext-devel
Ruby on Rails development package.

Edit and display rich text in Rails applications.

%description   -n gem-actiontext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actiontext.
%endif


%package       -n gem-actionpack
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionview) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(nokogiri) >= 1.8.5
Requires:      gem(racc) >= 0
Requires:      gem(rack) >= 2.2.4
Requires:      gem(rack-session) >= 1.0.1
Requires:      gem(rack-test) >= 0.6.3
Requires:      gem(rails-dom-testing) >= 2.2
Requires:      gem(rails-html-sanitizer) >= 1.6
Conflicts:     gem(rails-dom-testing) >= 3
Conflicts:     gem(rails-html-sanitizer) >= 2
Provides:      actionpack = %EVR
Provides:      gem(actionpack) = 7.1.5.1

%description   -n gem-actionpack
Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.


%if_enabled    doc
%package       -n gem-actionpack-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionpack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionpack) = 7.1.5.1

%description   -n gem-actionpack-doc
Ruby on Rails documentation files.

Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.

%description   -n gem-actionpack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionpack.
%endif


%if_enabled    devel
%package       -n gem-actionpack-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionpack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) = 7.1.5.1

%description   -n gem-actionpack-devel
Ruby on Rails development package.

Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.

%description   -n gem-actionpack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionpack.
%endif


%package       -n gem-activemodel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(activesupport) = 7.1.5.1
Provides:      activemodel = %EVR
Provides:      gem(activemodel) = 7.1.5.1

%description   -n gem-activemodel
A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.


%if_enabled    doc
%package       -n gem-activemodel-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activemodel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activemodel) = 7.1.5.1

%description   -n gem-activemodel-doc
Ruby on Rails documentation files.

A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.

%description   -n gem-activemodel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activemodel.
%endif


%if_enabled    devel
%package       -n gem-activemodel-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activemodel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activemodel) = 7.1.5.1

%description   -n gem-activemodel-devel
Ruby on Rails development package.

A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.

%description   -n gem-activemodel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activemodel.
%endif


%package       -n gem-actioncable
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(nio4r) >= 2.0
Requires:      gem(websocket-driver) >= 0.6.1
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(nio4r) >= 3
Conflicts:     gem(zeitwerk) >= 3
Provides:      actioncable = %EVR
Provides:      gem(actioncable) = 7.1.5.1

%description   -n gem-actioncable
Structure many real-time application concerns into channels over a single
WebSocket connection.


%if_enabled    doc
%package       -n gem-actioncable-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actioncable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actioncable) = 7.1.5.1

%description   -n gem-actioncable-doc
Ruby on Rails documentation files.

Structure many real-time application concerns into channels over a single
WebSocket connection.

%description   -n gem-actioncable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actioncable.
%endif


%if_enabled    devel
%package       -n gem-actioncable-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actioncable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actioncable) = 7.1.5.1

%description   -n gem-actioncable-devel
Ruby on Rails development package.

Structure many real-time application concerns into channels over a single
WebSocket connection.

%description   -n gem-actioncable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actioncable.
%endif


%package       -n gem-actionmailer
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) = 7.1.5.1
Requires:      gem(actionview) = 7.1.5.1
Requires:      gem(activejob) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(mail) >= 2.5.4
Requires:      gem(net-imap) >= 0
Requires:      gem(net-pop) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(rails-dom-testing) >= 2.2
Conflicts:     gem(mail) >= 3
Conflicts:     gem(rails-dom-testing) >= 3
Provides:      actionmailer = %EVR
Provides:      gem(actionmailer) = 7.1.5.1

%description   -n gem-actionmailer
Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.


%if_enabled    doc
%package       -n gem-actionmailer-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionmailer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionmailer) = 7.1.5.1

%description   -n gem-actionmailer-doc
Ruby on Rails documentation files.

Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%description   -n gem-actionmailer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionmailer.
%endif


%if_enabled    devel
%package       -n gem-actionmailer-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionmailer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionmailer) = 7.1.5.1

%description   -n gem-actionmailer-devel
Ruby on Rails development package.

Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%description   -n gem-actionmailer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionmailer.
%endif


%package       -n gem-activerecord
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(activemodel) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(timeout) >= 0.4.0
Provides:      activerecord = %EVR
Provides:      gem(activerecord) = 7.1.5.1

%description   -n gem-activerecord
Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.


%if_enabled    doc
%package       -n gem-activerecord-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord) = 7.1.5.1

%description   -n gem-activerecord-doc
Ruby on Rails documentation files.

Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.

%description   -n gem-activerecord-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord.
%endif


%if_enabled    devel
%package       -n gem-activerecord-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord) = 7.1.5.1

%description   -n gem-activerecord-devel
Ruby on Rails development package.

Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.

%description   -n gem-activerecord-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord.
%endif


%package       -n gem-activestorage
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) = 7.1.5.1
Requires:      gem(activejob) = 7.1.5.1
Requires:      gem(activerecord) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(marcel) >= 1.0
Conflicts:     gem(marcel) >= 2
Provides:      activestorage = %EVR
Provides:      gem(activestorage) = 7.1.5.1

%description   -n gem-activestorage
Attach cloud and local files in Rails applications.


%if_enabled    doc
%package       -n gem-activestorage-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activestorage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activestorage) = 7.1.5.1

%description   -n gem-activestorage-doc
Ruby on Rails documentation files.

Attach cloud and local files in Rails applications.

%description   -n gem-activestorage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activestorage.
%endif


%if_enabled    devel
%package       -n gem-activestorage-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activestorage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activestorage) = 7.1.5.1

%description   -n gem-activestorage-devel
Ruby on Rails development package.

Attach cloud and local files in Rails applications.

%description   -n gem-activestorage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activestorage.
%endif


%package       -n gem-activesupport
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(concurrent-ruby) >= 1.0.2
Requires:      gem(i18n) >= 1.6
Requires:      gem(minitest) >= 5.1
Requires:      gem(tzinfo) >= 2.0
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(i18n) >= 2
Conflicts:     gem(tzinfo) >= 3
Provides:      activesupport = %EVR
Provides:      gem(activesupport) = 7.1.5.1

%description   -n gem-activesupport
A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.


%if_enabled    doc
%package       -n gem-activesupport-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activesupport
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activesupport) = 7.1.5.1

%description   -n gem-activesupport-doc
Ruby on Rails documentation files.

A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.

%description   -n gem-activesupport-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activesupport.
%endif


%if_enabled    devel
%package       -n gem-activesupport-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activesupport
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 7.1.5.1

%description   -n gem-activesupport-devel
Ruby on Rails development package.

A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.

%description   -n gem-activesupport-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activesupport.
%endif


%package       -n gem-actionmailbox
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) = 7.1.5.1
Requires:      gem(activejob) = 7.1.5.1
Requires:      gem(activerecord) = 7.1.5.1
Requires:      gem(activestorage) = 7.1.5.1
Requires:      gem(activesupport) = 7.1.5.1
Requires:      gem(mail) >= 2.7.1
Requires:      gem(net-imap) >= 0
Requires:      gem(net-pop) >= 0
Requires:      gem(net-smtp) >= 0
Provides:      actionmailbox = %EVR
Provides:      gem(actionmailbox) = 7.1.5.1

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


%if_enabled    doc
%package       -n gem-actionmailbox-doc
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionmailbox
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionmailbox) = 7.1.5.1

%description   -n gem-actionmailbox-doc
Ruby on Rails documentation files.

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
%endif


%if_enabled    devel
%package       -n gem-actionmailbox-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionmailbox
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionmailbox) = 7.1.5.1

%description   -n gem-actionmailbox-devel
Ruby on Rails development package.

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
%endif


%package       -n gem-releaser
Version:       1.0.0
Release:       alt1
Summary:       Library to release Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 13.0
Conflicts:     gem(rake) >= 14
Provides:      gem(releaser) = 1.0.0

%description   -n gem-releaser
A set of tasks to release Rails


%if_enabled    doc
%package       -n gem-releaser-doc
Version:       1.0.0
Release:       alt1
Summary:       Library to release Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета releaser
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(releaser) = 1.0.0

%description   -n gem-releaser-doc
Library to release Rails documentation files.

A set of tasks to release Rails

%description   -n gem-releaser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета releaser.
%endif


%if_enabled    devel
%package       -n gem-releaser-devel
Version:       1.0.0
Release:       alt1
Summary:       Library to release Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета releaser
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(releaser) = 1.0.0

%description   -n gem-releaser-devel
Library to release Rails development package.

A set of tasks to release Rails

%description   -n gem-releaser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета releaser.
%endif


%package       -n gem-rail-inspector
Version:       0.0.2
Release:       alt1
Summary:       A collection of linters for rails/rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 2.7.0
Requires:      gem(syntax_tree) >= 6.1.1
Requires:      gem(thor) >= 1.0
Conflicts:     gem(thor) >= 2
Provides:      gem(rail_inspector) = 0.0.2

%description   -n gem-rail-inspector
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


%if_enabled    doc
%package       -n gem-rail-inspector-doc
Version:       0.0.2
Release:       alt1
Summary:       A collection of linters for rails/rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rail_inspector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rail_inspector) = 0.0.2

%description   -n gem-rail-inspector-doc
A collection of linters for rails/rails documentation files.

Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

%description   -n gem-rail-inspector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rail_inspector.
%endif


%if_enabled    devel
%package       -n gem-rail-inspector-devel
Version:       0.0.2
Release:       alt1
Summary:       A collection of linters for rails/rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rail_inspector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rail_inspector) = 0.0.2

%description   -n gem-rail-inspector-devel
A collection of linters for rails/rails development package.

Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

%description   -n gem-rail-inspector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rail_inspector.
%endif


%if_enabled    devel
%package       -n gem-rails-devel
Version:       7.1.5.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails) = 7.1.5.1
Requires:      gem(minitest-bisect) >= 0
Requires:      gem(minitest-ci) >= 0
Requires:      gem(minitest-retry) >= 0
Requires:      gem(aws-sdk-sns) >= 0
Requires:      gem(bcrypt) >= 3.1.11
Requires:      gem(bootsnap) >= 1.4.4
Requires:      gem(bundler) >= 1.15.0
Requires:      gem(capybara) >= 3.39
Requires:      gem(cgi) >= 0.3.6
Requires:      gem(connection_pool) >= 0
Requires:      gem(cssbundling-rails) >= 0
Requires:      gem(dalli) >= 3.0.1
Requires:      gem(dartsass-rails) >= 0
Requires:      gem(importmap-rails) > 2.0.2
Requires:      gem(jbuilder) >= 0
Requires:      gem(jsbundling-rails) >= 0
Requires:      gem(json) > 2.7.0
Requires:      gem(libxml-ruby) >= 0
Requires:      gem(listen) >= 3.3
Requires:      gem(minitest) >= 0
Requires:      gem(msgpack) >= 1.7.0
Requires:      gem(nokogiri) > 1.11.0
Requires:      gem(propshaft) >= 0.1.7
Requires:      gem(racc) >= 1.4.6
Requires:      gem(rack) >= 3.0
Requires:      gem(rack-cache) >= 1.2
Requires:      gem(rake) >= 13
Requires:      gem(rexml) >= 0
Requires:      gem(selenium-webdriver) >= 4.11.0
Requires:      gem(sprockets-rails) >= 2.0.0
Requires:      gem(sqlite3) >= 1.6.6
Requires:      gem(stimulus-rails) >= 0
Requires:      gem(tailwindcss-rails) >= 0
Requires:      gem(terser) >= 1.1.4
Requires:      gem(turbo-rails) >= 0
Requires:      gem(web-console) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(webrick) >= 0
Conflicts:     gem(bcrypt) >= 3.2
Conflicts:     gem(listen) >= 4
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rack-cache) >= 2

%description   -n gem-rails-devel
Ruby on Rails development package.

Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

%description   -n gem-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails.
%endif

%global        version 7.1.5.1

%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc MIT-LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-railties
%doc MIT-LICENSE
%ruby_gemspecdir/railties-7.1.5.1.gemspec
%ruby_gemslibdir/railties-7.1.5.1

%files         -n rails
%doc MIT-LICENSE
%_bindir/rails

%if_enabled    doc
%files         -n gem-railties-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/railties-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-railties-devel
%doc MIT-LICENSE
%endif

%files         -n gem-activejob
%doc MIT-LICENSE README.md
%ruby_gemspecdir/activejob-7.1.5.1.gemspec
%ruby_gemslibdir/activejob-7.1.5.1

%if_enabled    doc
%files         -n gem-activejob-doc
%doc MIT-LICENSE README.md
%ruby_gemsdocdir/activejob-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-activejob-devel
%doc MIT-LICENSE README.md
%endif

%files         -n gem-actionview
%doc MIT-LICENSE
%ruby_gemspecdir/actionview-7.1.5.1.gemspec
%ruby_gemslibdir/actionview-7.1.5.1

%if_enabled    doc
%files         -n gem-actionview-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/actionview-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-actionview-devel
%doc MIT-LICENSE
%endif

%files         -n gem-actiontext
%doc MIT-LICENSE README.md
%ruby_gemspecdir/actiontext-7.1.5.1.gemspec
%ruby_gemslibdir/actiontext-7.1.5.1

%if_enabled    doc
%files         -n gem-actiontext-doc
%doc MIT-LICENSE README.md
%ruby_gemsdocdir/actiontext-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-actiontext-devel
%doc MIT-LICENSE README.md
%endif

%files         -n gem-actionpack
%doc MIT-LICENSE
%ruby_gemspecdir/actionpack-7.1.5.1.gemspec
%ruby_gemslibdir/actionpack-7.1.5.1

%if_enabled    doc
%files         -n gem-actionpack-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/actionpack-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-actionpack-devel
%doc MIT-LICENSE
%endif

%files         -n gem-activemodel
%doc MIT-LICENSE
%ruby_gemspecdir/activemodel-7.1.5.1.gemspec
%ruby_gemslibdir/activemodel-7.1.5.1

%if_enabled    doc
%files         -n gem-activemodel-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/activemodel-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-activemodel-devel
%doc MIT-LICENSE
%endif

%files         -n gem-actioncable
%doc MIT-LICENSE README.md
%ruby_gemspecdir/actioncable-7.1.5.1.gemspec
%ruby_gemslibdir/actioncable-7.1.5.1

%if_enabled    doc
%files         -n gem-actioncable-doc
%doc MIT-LICENSE README.md
%ruby_gemsdocdir/actioncable-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-actioncable-devel
%doc MIT-LICENSE README.md
%endif

%files         -n gem-actionmailer
%doc MIT-LICENSE
%ruby_gemspecdir/actionmailer-7.1.5.1.gemspec
%ruby_gemslibdir/actionmailer-7.1.5.1

%if_enabled    doc
%files         -n gem-actionmailer-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/actionmailer-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-actionmailer-devel
%doc MIT-LICENSE
%endif

%files         -n gem-activerecord
%doc MIT-LICENSE
%ruby_gemspecdir/activerecord-7.1.5.1.gemspec
%ruby_gemslibdir/activerecord-7.1.5.1

%if_enabled    doc
%files         -n gem-activerecord-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/activerecord-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-activerecord-devel
%doc MIT-LICENSE
%endif

%files         -n gem-activestorage
%doc MIT-LICENSE README.md
%ruby_gemspecdir/activestorage-7.1.5.1.gemspec
%ruby_gemslibdir/activestorage-7.1.5.1

%if_enabled    doc
%files         -n gem-activestorage-doc
%doc MIT-LICENSE README.md
%ruby_gemsdocdir/activestorage-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-activestorage-devel
%doc MIT-LICENSE README.md
%endif

%files         -n gem-activesupport
%doc MIT-LICENSE
%ruby_gemspecdir/activesupport-7.1.5.1.gemspec
%ruby_gemslibdir/activesupport-7.1.5.1

%if_enabled    doc
%files         -n gem-activesupport-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/activesupport-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-activesupport-devel
%doc MIT-LICENSE
%endif

%files         -n gem-actionmailbox
%doc MIT-LICENSE README.md
%ruby_gemspecdir/actionmailbox-7.1.5.1.gemspec
%ruby_gemslibdir/actionmailbox-7.1.5.1

%if_enabled    doc
%files         -n gem-actionmailbox-doc
%doc MIT-LICENSE README.md
%ruby_gemsdocdir/actionmailbox-7.1.5.1
%endif

%if_enabled    devel
%files         -n gem-actionmailbox-devel
%doc MIT-LICENSE README.md
%endif

%files         -n gem-releaser
%doc README.md
%ruby_gemspecdir/releaser-1.0.0.gemspec
%ruby_gemslibdir/releaser-1.0.0

%if_enabled    doc
%files         -n gem-releaser-doc
%doc README.md
%ruby_gemsdocdir/releaser-1.0.0
%endif

%if_enabled    devel
%files         -n gem-releaser-devel
%doc README.md
%endif

%files         -n gem-rail-inspector
%ruby_gemspecdir/rail_inspector-0.0.2.gemspec
%ruby_gemslibdir/rail_inspector-0.0.2

%if_enabled    doc
%files         -n gem-rail-inspector-doc
%ruby_gemsdocdir/rail_inspector-0.0.2
%endif

%if_enabled    devel
%files         -n gem-rail-inspector-devel
%endif

%if_enabled    devel
%files         -n gem-rails-devel
%doc MIT-LICENSE README.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 7.1.5.1-alt1
- ^ 6.1.7.8 -> 7.1.5.1
- ! CVEs
 + CVE-2024-54133
 + CVE-2024-53847
 + CVE-2024-47889
 + CVE-2024-47888
 + CVE-2024-41128
 + CVE-2024-47887
 + CVE-2024-32464
 + CVE-2024-28103
 + CVE-2024-26143
 + CVE-2024-26142
 + CVE-2013-0276

* Tue Aug 20 2024 Pavel Skrylev <majioa@altlinux.org> 6.1.7.8-alt1
- ^ 6.1.7.7 -> 6.1.7.8
- - droppen railsctl binary in favor of separated package
- ! fixed CVE-2024-28103
- ! psych dep

* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 6.1.7.7-alt1
- ^ 6.1.7.1 -> 6.1.7.7
- ! CVEs
 + CVE-2024-26144
 + CVE-2023-38037
 + CVE-2023-28362
 + CVE-2023-23913

* Tue Apr 02 2024 Pavel Vasenkov <pav@altlinux.org> 6.1.7.1-alt1.2
- ! add path to bundle

* Wed Feb 22 2023 Pavel Skrylev <majioa@altlinux.org> 6.1.7.1-alt1.1
- ! rolled back lost railsctl

* Fri Jan 20 2023 Pavel Skrylev <majioa@altlinux.org> 6.1.7.1-alt1
- ^ 6.1.7 -> 6.1.7.1
- ! CVEs
 + CVE-2023-22794
 + CVE-2023-22795
 + CVE-2023-22796
 + CVE-2023-22792
 + CVE-2022-44566

* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.7-alt1.1
- * change bundle's rails env to use BUNDLE_GEMFILE var for the railsctl
- * change bundle's install to update function for the railsctl

* Thu Oct 06 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.7-alt1
- ^ 6.1.6.1 -> 6.1.7

* Thu Sep 01 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.6.1-alt1
- ^ 6.1.4.1 -> 6.1.6.1
- ! CVEs
 + CVE-2022-32224
 + CVE-2022-27777
 + CVE-2022-21831
 + CVE-2022-23633
 + CVE-2022-23633
 + CVE-2021-44528

* Tue Oct 26 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.4.1-alt1.1
- - disabling the wepback:compile and assers:precompile for the railsctl

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.4.1-alt1
- ^ 6.1.3.2 -> 6.1.4.1

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

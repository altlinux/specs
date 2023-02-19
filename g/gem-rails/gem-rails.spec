%define        gemname rails

Name:          gem-rails
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://rubyonrails.org/
Vcs:           https://github.com/rails/rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source1:       railsctl
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.15.0 gem(minitest) < 6
BuildRequires: gem(cgi) >= 0.3.6
BuildRequires: gem(rake) >= 13
BuildRequires: gem(capybara) >= 3.26
BuildRequires: gem(selenium-webdriver) >= 4.0.0.alpha7 gem(selenium-webdriver) < 4.2
BuildRequires: gem(rack-cache) >= 1.2 gem(rack-cache) < 2
BuildRequires: gem(sass-rails) >= 0
BuildRequires: gem(turbolinks) >= 5 gem(turbolinks) < 6
BuildRequires: gem(webpacker) >= 5.0 gem(webpacker) < 6
BuildRequires: gem(bcrypt) >= 3.1.11 gem(bcrypt) < 3.2
BuildRequires: gem(uglifier) >= 1.3.0
BuildRequires: gem(json) >= 2.0.0
BuildRequires: gem(rack-test) < 2
BuildRequires: gem(rubocop) >= 0.90
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(sdoc) >= 2.3.0
BuildRequires: gem(redcarpet) >= 3.2.3 gem(redcarpet) < 3.3
BuildRequires: gem(w3c_validators) >= 1.3.6 gem(w3c_validators) < 1.4
BuildRequires: gem(kindlerb) >= 1.2.0 gem(kindlerb) < 1.3
BuildRequires: gem(rouge) >= 0
BuildRequires: gem(dalli) >= 0
BuildRequires: gem(listen) >= 3.3 gem(listen) < 4
BuildRequires: gem(libxml-ruby) >= 0
BuildRequires: gem(connection_pool) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(bootsnap) >= 1.4.4
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(resque) >= 0
BuildRequires: gem(resque-scheduler) >= 0
BuildRequires: gem(sidekiq) >= 0
BuildRequires: gem(sucker_punch) >= 0
BuildRequires: gem(delayed_job) >= 0
BuildRequires: gem(sneakers) >= 0
BuildRequires: gem(que) < 2
BuildRequires: gem(backburner) >= 0
BuildRequires: gem(delayed_job_active_record) >= 0
BuildRequires: gem(sequel) >= 0
BuildRequires: gem(puma) >= 5.0.3
BuildRequires: gem(hiredis) >= 0
BuildRequires: gem(redis) >= 4.0 gem(redis) < 5
BuildRequires: gem(blade) >= 0
BuildRequires: gem(blade-sauce_labs_plugin) >= 0
BuildRequires: gem(sprockets-export) >= 0
BuildRequires: gem(aws-sdk-s3) >= 0
BuildRequires: gem(google-cloud-storage) >= 1.11 gem(google-cloud-storage) < 2
BuildRequires: gem(azure-storage-blob) >= 0
BuildRequires: gem(image_processing) >= 1.2 gem(image_processing) < 2
BuildRequires: gem(aws-sdk-sns) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(webdrivers) >= 0
BuildRequires: gem(minitest-bisect) >= 0
BuildRequires: gem(minitest-retry) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(nokogiri) >= 1.8.1
BuildRequires: gem(racc) >= 1.4.6
BuildRequires: gem(sqlite3) >= 1.4 gem(sqlite3) < 2
BuildRequires: gem(pg) >= 1.3.0.rc1
BuildRequires: gem(psych) >= 3.0 gem(psych) < 4
BuildRequires: gem(wdm) >= 0.1.0
BuildRequires: gem(net-smtp) >= 0
BuildRequires: gem(net-imap) >= 0
BuildRequires: gem(net-pop) >= 0
BuildRequires: gem(digest) >= 3.1.0 gem(digest) < 3.2
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(bundler) >= 1.15.0
BuildRequires: gem(sprockets-rails) >= 2.0.0
BuildRequires: gem(rake) >= 12.2
BuildRequires: gem(thor) >= 1.0 gem(thor) < 2
BuildRequires: gem(method_source) >= 0
BuildRequires: gem(globalid) >= 0.3.6
BuildRequires: gem(builder) >= 3.1 gem(builder) < 4
BuildRequires: gem(erubi) >= 1.4 gem(erubi) < 2
BuildRequires: gem(rails-html-sanitizer) >= 1.2.0 gem(rails-html-sanitizer) < 2
BuildRequires: gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
BuildRequires: gem(nokogiri) >= 1.8.5
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rack-test) >= 0.6.3
BuildRequires: gem(nio4r) >= 2.0 gem(nio4r) < 3
BuildRequires: gem(websocket-driver) >= 0.6.1
BuildRequires: gem(mail) >= 2.5.4 gem(mail) < 3
BuildRequires: gem(mail) >= 2.7.1
BuildRequires: gem(i18n) >= 1.6 gem(i18n) < 2
BuildRequires: gem(tzinfo) >= 2.0 gem(tzinfo) < 3
BuildRequires: gem(concurrent-ruby) >= 1.0.2 gem(concurrent-ruby) < 2
BuildRequires: gem(zeitwerk) >= 2.3 gem(zeitwerk) < 3
BuildRequires: gem(marcel) >= 1.0 gem(marcel) < 2
BuildRequires: gem(mini_mime) >= 1.1.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(actionview) = 6.1.7.1
Requires:      gem(activemodel) = 6.1.7.1
Requires:      gem(activerecord) = 6.1.7.1
Requires:      gem(actionmailer) = 6.1.7.1
Requires:      gem(activejob) = 6.1.7.1
Requires:      gem(actioncable) = 6.1.7.1
Requires:      gem(activestorage) = 6.1.7.1
Requires:      gem(actionmailbox) = 6.1.7.1
Requires:      gem(actiontext) = 6.1.7.1
Requires:      gem(railties) = 6.1.7.1
Requires:      gem(bundler) >= 1.15.0
Requires:      gem(sprockets-rails) >= 2.0.0
Requires:      rails = %EVR
Obsoletes:     ruby-rails < %EVR
Provides:      ruby-rails = %EVR
Provides:      gem(rails) = 6.1.7.1


%description
Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.


%package       -n gem-railties
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(rake) >= 12.2
Requires:      gem(thor) >= 1.0 gem(thor) < 2
Requires:      gem(method_source) >= 0
Provides:      gem(railties) = 6.1.7.1

%description   -n gem-railties
Rails internals: application bootup, plugins, generators, and rake tasks.


%package       -n rails
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета railties
Group:         Other
BuildArch:     noarch

Requires:      gem(railties) = 6.1.7.1

%description   -n rails
Ruby on Rails executable(s).

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n rails -l ru_RU.UTF-8
Исполнямка для самоцвета railties.


%package       -n gem-railties-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета railties
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(railties) = 6.1.7.1

%description   -n gem-railties-doc
Ruby on Rails documentation files.

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n gem-railties-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета railties.


%package       -n gem-railties-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета railties
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(railties) = 6.1.7.1
Requires:      gem(actionview) = 6.1.7.1

%description   -n gem-railties-devel
Ruby on Rails development package.

Rails internals: application bootup, plugins, generators, and rake tasks.

%description   -n gem-railties-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета railties.


%package       -n gem-activejob
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(globalid) >= 0.3.6
Provides:      gem(activejob) = 6.1.7.1

%description   -n gem-activejob
Declare job classes that can be run by a variety of queuing backends.


%package       -n gem-activejob-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activejob
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activejob) = 6.1.7.1

%description   -n gem-activejob-doc
Ruby on Rails documentation files.

Declare job classes that can be run by a variety of queuing backends.

%description   -n gem-activejob-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activejob.


%package       -n gem-activejob-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activejob
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activejob) = 6.1.7.1

%description   -n gem-activejob-devel
Ruby on Rails development package.

Declare job classes that can be run by a variety of queuing backends.

%description   -n gem-activejob-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activejob.


%package       -n gem-actionview
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(builder) >= 3.1 gem(builder) < 4
Requires:      gem(erubi) >= 1.4 gem(erubi) < 2
Requires:      gem(rails-html-sanitizer) >= 1.2.0 gem(rails-html-sanitizer) < 2
Requires:      gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
Provides:      gem(actionview) = 6.1.7.1

%description   -n gem-actionview
Simple, battle-tested conventions and helpers for building web pages.


%package       -n gem-actionview-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionview
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionview) = 6.1.7.1

%description   -n gem-actionview-doc
Ruby on Rails documentation files.

Simple, battle-tested conventions and helpers for building web pages.

%description   -n gem-actionview-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionview.


%package       -n gem-actionview-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionview
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionview) = 6.1.7.1
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(activemodel) = 6.1.7.1

%description   -n gem-actionview-devel
Ruby on Rails development package.

Simple, battle-tested conventions and helpers for building web pages.

%description   -n gem-actionview-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionview.


%package       -n gem-actiontext
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(activerecord) = 6.1.7.1
Requires:      gem(activestorage) = 6.1.7.1
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(nokogiri) >= 1.8.5
Provides:      gem(actiontext) = 6.1.7.1

%description   -n gem-actiontext
Edit and display rich text in Rails applications.


%package       -n gem-actiontext-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actiontext
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actiontext) = 6.1.7.1

%description   -n gem-actiontext-doc
Ruby on Rails documentation files.

Edit and display rich text in Rails applications.

%description   -n gem-actiontext-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actiontext.


%package       -n gem-actiontext-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actiontext
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actiontext) = 6.1.7.1

%description   -n gem-actiontext-devel
Ruby on Rails development package.

Edit and display rich text in Rails applications.

%description   -n gem-actiontext-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actiontext.


%package       -n gem-actionpack
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(rack) >= 2.0
Requires:      gem(rack-test) >= 0.6.3
Requires:      gem(rails-html-sanitizer) >= 1.2.0 gem(rails-html-sanitizer) < 2
Requires:      gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
Requires:      gem(actionview) = 6.1.7.1
Provides:      gem(actionpack) = 6.1.7.1

%description   -n gem-actionpack
Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.


%package       -n gem-actionpack-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionpack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionpack) = 6.1.7.1

%description   -n gem-actionpack-doc
Ruby on Rails documentation files.

Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.

%description   -n gem-actionpack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionpack.


%package       -n gem-actionpack-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionpack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(activemodel) = 6.1.7.1

%description   -n gem-actionpack-devel
Ruby on Rails development package.

Web apps on Rails. Simple, battle-tested conventions for building and testing
MVC web applications. Works with any Rack-compatible server.

%description   -n gem-actionpack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionpack.


%package       -n gem-actioncable
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(nio4r) >= 2.0 gem(nio4r) < 3
Requires:      gem(websocket-driver) >= 0.6.1
Provides:      gem(actioncable) = 6.1.7.1

%description   -n gem-actioncable
Structure many real-time application concerns into channels over a single
WebSocket connection.


%package       -n gem-actioncable-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actioncable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actioncable) = 6.1.7.1

%description   -n gem-actioncable-doc
Ruby on Rails documentation files.

Structure many real-time application concerns into channels over a single
WebSocket connection.

%description   -n gem-actioncable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actioncable.


%package       -n gem-actioncable-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actioncable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actioncable) = 6.1.7.1

%description   -n gem-actioncable-devel
Ruby on Rails development package.

Structure many real-time application concerns into channels over a single
WebSocket connection.

%description   -n gem-actioncable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actioncable.


%package       -n gem-activemodel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Provides:      gem(activemodel) = 6.1.7.1

%description   -n gem-activemodel
A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.


%package       -n gem-activemodel-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activemodel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activemodel) = 6.1.7.1

%description   -n gem-activemodel-doc
Ruby on Rails documentation files.

A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.

%description   -n gem-activemodel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activemodel.


%package       -n gem-activemodel-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activemodel
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activemodel) = 6.1.7.1

%description   -n gem-activemodel-devel
Ruby on Rails development package.

A toolkit for building modeling frameworks like Active Record. Rich support for
attributes, callbacks, validations, serialization, internationalization, and
testing.

%description   -n gem-activemodel-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activemodel.


%package       -n gem-actionmailer
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(actionview) = 6.1.7.1
Requires:      gem(activejob) = 6.1.7.1
Requires:      gem(mail) >= 2.5.4 gem(mail) < 3
Requires:      gem(rails-dom-testing) >= 2.0 gem(rails-dom-testing) < 3
Provides:      gem(actionmailer) = 6.1.7.1

%description   -n gem-actionmailer
Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.


%package       -n gem-actionmailer-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionmailer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionmailer) = 6.1.7.1

%description   -n gem-actionmailer-doc
Ruby on Rails documentation files.

Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%description   -n gem-actionmailer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета actionmailer.


%package       -n gem-actionmailer-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionmailer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionmailer) = 6.1.7.1

%description   -n gem-actionmailer-devel
Ruby on Rails development package.

Email on Rails. Compose, deliver, and test emails using the familiar
controller/view pattern. First-class support for multipart email and
attachments.

%description   -n gem-actionmailer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета actionmailer.


%package       -n gem-activerecord
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(activemodel) = 6.1.7.1
Provides:      gem(activerecord) = 6.1.7.1

%description   -n gem-activerecord
Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.


%package       -n gem-activerecord-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord) = 6.1.7.1

%description   -n gem-activerecord-doc
Ruby on Rails documentation files.

Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.

%description   -n gem-activerecord-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord.


%package       -n gem-activerecord-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord) = 6.1.7.1

%description   -n gem-activerecord-devel
Ruby on Rails development package.

Databases on Rails. Build a persistent domain model by mapping database tables
to Ruby classes. Strong conventions for associations, validations, aggregations,
migrations, and testing come baked-in.

%description   -n gem-activerecord-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord.


%package       -n gem-actionmailbox
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(activerecord) = 6.1.7.1
Requires:      gem(activestorage) = 6.1.7.1
Requires:      gem(activejob) = 6.1.7.1
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(mail) >= 2.7.1
Provides:      gem(actionmailbox) = 6.1.7.1

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
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета actionmailbox
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(actionmailbox) = 6.1.7.1

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


%package       -n gem-actionmailbox-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета actionmailbox
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(actionmailbox) = 6.1.7.1

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


%package       -n gem-activesupport
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(i18n) >= 1.6 gem(i18n) < 2
Requires:      gem(tzinfo) >= 2.0 gem(tzinfo) < 3
Requires:      gem(concurrent-ruby) >= 1.0.2 gem(concurrent-ruby) < 2
Requires:      gem(zeitwerk) >= 2.3 gem(zeitwerk) < 3
Requires:      gem(minitest) >= 5.1
Provides:      gem(activesupport) = 6.1.7.1

%description   -n gem-activesupport
A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.


%package       -n gem-activesupport-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activesupport
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.7.1

%description   -n gem-activesupport-doc
Ruby on Rails documentation files.

A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.

%description   -n gem-activesupport-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activesupport.


%package       -n gem-activesupport-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activesupport
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) = 6.1.7.1

%description   -n gem-activesupport-devel
Ruby on Rails development package.

A toolkit of support libraries and Ruby core extensions extracted from the Rails
framework. Rich support for multibyte strings, internationalization, time zones,
and testing.

%description   -n gem-activesupport-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activesupport.


%package       -n gem-activestorage
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 6.1.3.2 gem(activesupport) < 7
Requires:      gem(actionpack) = 6.1.7.1
Requires:      gem(activejob) = 6.1.7.1
Requires:      gem(activerecord) = 6.1.7.1
Requires:      gem(marcel) >= 1.0 gem(marcel) < 2
Requires:      gem(mini_mime) >= 1.1.0
Provides:      gem(activestorage) = 6.1.7.1

%description   -n gem-activestorage
Attach cloud and local files in Rails applications.


%package       -n gem-activestorage-doc
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activestorage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activestorage) = 6.1.7.1

%description   -n gem-activestorage-doc
Ruby on Rails documentation files.

Attach cloud and local files in Rails applications.

%description   -n gem-activestorage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activestorage.


%package       -n gem-activestorage-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activestorage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activestorage) = 6.1.7.1

%description   -n gem-activestorage-devel
Ruby on Rails development package.

Attach cloud and local files in Rails applications.

%description   -n gem-activestorage-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activestorage.


%package       -n gem-rails-devel
Version:       6.1.7.1
Release:       alt1
Summary:       Ruby on Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails) = 6.1.7.1

%description   -n gem-rails-devel
Ruby on Rails development package.

Ruby on Rails is a full-stack web framework optimized for programmer happiness
and sustainable productivity. It encourages beautiful code by favoring
convention over configuration.

%description   -n gem-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-railties
%doc README.md
%ruby_gemspecdir/railties-6.1.7.1.gemspec
%ruby_gemslibdir/railties-6.1.7.1

%files         -n rails
%doc README.md
%_bindir/rails

%files         -n gem-railties-doc
%doc README.md
%ruby_gemsdocdir/railties-6.1.7.1

%files         -n gem-railties-devel
%doc README.md

%files         -n gem-activejob
%doc README.md
%ruby_gemspecdir/activejob-6.1.7.1.gemspec
%ruby_gemslibdir/activejob-6.1.7.1

%files         -n gem-activejob-doc
%doc README.md
%ruby_gemsdocdir/activejob-6.1.7.1

%files         -n gem-activejob-devel
%doc README.md

%files         -n gem-actionview
%doc README.md
%ruby_gemspecdir/actionview-6.1.7.1.gemspec
%ruby_gemslibdir/actionview-6.1.7.1

%files         -n gem-actionview-doc
%doc README.md
%ruby_gemsdocdir/actionview-6.1.7.1

%files         -n gem-actionview-devel
%doc README.md

%files         -n gem-actiontext
%doc README.md
%ruby_gemspecdir/actiontext-6.1.7.1.gemspec
%ruby_gemslibdir/actiontext-6.1.7.1

%files         -n gem-actiontext-doc
%doc README.md
%ruby_gemsdocdir/actiontext-6.1.7.1

%files         -n gem-actiontext-devel
%doc README.md

%files         -n gem-actionpack
%doc README.md
%ruby_gemspecdir/actionpack-6.1.7.1.gemspec
%ruby_gemslibdir/actionpack-6.1.7.1

%files         -n gem-actionpack-doc
%doc README.md
%ruby_gemsdocdir/actionpack-6.1.7.1

%files         -n gem-actionpack-devel
%doc README.md

%files         -n gem-actioncable
%doc README.md
%ruby_gemspecdir/actioncable-6.1.7.1.gemspec
%ruby_gemslibdir/actioncable-6.1.7.1

%files         -n gem-actioncable-doc
%doc README.md
%ruby_gemsdocdir/actioncable-6.1.7.1

%files         -n gem-actioncable-devel
%doc README.md

%files         -n gem-activemodel
%doc README.md
%ruby_gemspecdir/activemodel-6.1.7.1.gemspec
%ruby_gemslibdir/activemodel-6.1.7.1

%files         -n gem-activemodel-doc
%doc README.md
%ruby_gemsdocdir/activemodel-6.1.7.1

%files         -n gem-activemodel-devel
%doc README.md

%files         -n gem-actionmailer
%doc README.md
%ruby_gemspecdir/actionmailer-6.1.7.1.gemspec
%ruby_gemslibdir/actionmailer-6.1.7.1

%files         -n gem-actionmailer-doc
%doc README.md
%ruby_gemsdocdir/actionmailer-6.1.7.1

%files         -n gem-actionmailer-devel
%doc README.md

%files         -n gem-activerecord
%doc README.md
%ruby_gemspecdir/activerecord-6.1.7.1.gemspec
%ruby_gemslibdir/activerecord-6.1.7.1

%files         -n gem-activerecord-doc
%doc README.md
%ruby_gemsdocdir/activerecord-6.1.7.1

%files         -n gem-activerecord-devel
%doc README.md

%files         -n gem-actionmailbox
%doc README.md
%ruby_gemspecdir/actionmailbox-6.1.7.1.gemspec
%ruby_gemslibdir/actionmailbox-6.1.7.1

%files         -n gem-actionmailbox-doc
%doc README.md
%ruby_gemsdocdir/actionmailbox-6.1.7.1

%files         -n gem-actionmailbox-devel
%doc README.md

%files         -n gem-activesupport
%doc README.md
%ruby_gemspecdir/activesupport-6.1.7.1.gemspec
%ruby_gemslibdir/activesupport-6.1.7.1

%files         -n gem-activesupport-doc
%doc README.md
%ruby_gemsdocdir/activesupport-6.1.7.1

%files         -n gem-activesupport-devel
%doc README.md

%files         -n gem-activestorage
%doc README.md
%ruby_gemspecdir/activestorage-6.1.7.1.gemspec
%ruby_gemslibdir/activestorage-6.1.7.1

%files         -n gem-activestorage-doc
%doc README.md
%ruby_gemsdocdir/activestorage-6.1.7.1

%files         -n gem-activestorage-devel
%doc README.md

%files         -n gem-rails-devel
%doc README.md


%changelog
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

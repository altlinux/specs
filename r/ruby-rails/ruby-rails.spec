%define        pkgname rails

Name:          ruby-%pkgname
Version:       5.2.2.1
Release:       alt1
Summary:       Ruby on Rails
License:       MIT
Group:         Development/Ruby
Url:           https://rubyonrails.org/
# VCS:         https://github.com/rails/rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
Ruby on Rails metapackage gem.

%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch
Provides:      activerecord-gems-doc = %EVR
Obsoletes:     activerecord-gems-doc < %EVR
Provides:      activesupport-gems-doc = %EVR
Obsoletes:     activesupport-gems-doc < %EVR

%description   doc
Documentation files for %{name}.


%package       -n ruby-actioncable
Summary:       WebSocket framework for Rails
Group:         Development/Ruby

%description   -n ruby-actioncable
Structure many real-time application concerns into channels over a
single WebSocket connection.


%package       -n ruby-actioncable-doc
Summary:       Documentation files for "ruby-actioncable" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-actioncable-doc
%summary


%package       -n ruby-actionmailer
Summary:       Email composition, delivery, and receiving framework (part of Rails)
Group:         Development/Ruby

%description   -n ruby-actionmailer
Email on Rails. Compose, deliver, receive, and test emails using the
familiar controller/view pattern. First-class support for multipart
email and attachments.


%package       -n ruby-actionmailer-doc
Summary:       Documentation files for "ruby-actionmailer" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-actionmailer-doc
%summary


%package       -n ruby-actionpack
Summary:       Web-flow and rendering framework putting the VC in MVC (part of Rails)
Group:         Development/Ruby

%description   -n ruby-actionpack
Web apps on Rails. Simple, battle-tested conventions for building and
testing MVC web applications. Works with any Rack-compatible server.


%package       -n ruby-actionpack-doc
Summary:       Documentation files for "ruby-actionpack" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-actionpack-doc
%summary


%package       -n ruby-actionview
Summary:       Rendering framework putting the V in MVC (part of Rails)
Group:         Development/Ruby

%description   -n ruby-actionview
Simple, battle-tested conventions and helpers for building web pages.


%package       -n ruby-actionview-doc
Summary:       Documentation files for "ruby-actionview" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-actionview-doc
%summary


%package       -n ruby-activejob
Summary:       Job framework with pluggable queues
Group:         Development/Ruby

%description   -n ruby-activejob
Declare job classes that can be run by a variety of queueing backends.


%package       -n ruby-activejob-doc
Summary:       Documentation files for "ruby-activejob" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-activejob-doc
%summary


%package       -n ruby-activemodel
Summary:       A toolkit for building modeling frameworks (part of Rails)
Group:         Development/Ruby

%description   -n ruby-activemodel
A toolkit for building modeling frameworks like Active Record. Rich
support for attributes, callbacks, validations, serialization,
internationalization, and testing.


%package       -n ruby-activemodel-doc
Summary:       Documentation files for "ruby-activemodel" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-activemodel-doc
%summary


%package       -n ruby-activerecord
Summary:       Object-relational mapper framework (part of Rails)
Group:         Development/Ruby
Provides:      activerecord-gems = %EVR
Obsoletes:     activerecord-gems < %EVR

%description   -n ruby-activerecord
Databases on Rails. Build a persistent domain model by mapping database
tables to Ruby classes. Strong conventions for associations,
validations, aggregations, migrations, and testing come baked-in.


%package       -n ruby-activerecord-doc
Summary:       Documentation files for "ruby-activerecord" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-activerecord-doc
%summary


%package       -n ruby-activestorage
Summary:       Local and cloud file storage framework
Group:         Development/Ruby

%description   -n ruby-activestorage
Attach cloud and local files in Rails applications.


%package       -n ruby-activestorage-doc
Summary:       Documentation files for "ruby-activestorage" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-activestorage-doc
%summary


%package       -n ruby-activesupport
Summary:       A toolkit of support libraries and Ruby core extensions extracted from the Rails framework
Group:         Development/Ruby
Provides:      activesupport-gems = %EVR
Obsoletes:     activesupport-gems < %EVR

%description   -n ruby-activesupport
A toolkit of support libraries and Ruby core extensions extracted from
the Rails framework. Rich support for multibyte strings,
internationalization, time zones, and testing.


%package       -n ruby-activesupport-doc
Summary:       Documentation files for "ruby-activesupport" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-activesupport-doc
%summary


%package       -n ruby-railties
Summary:       Tools for creating, working with, and running Rails applications
Group:         Development/Ruby

%description   -n ruby-railties
Rails internals: application bootup, plugins, generators, and rake tasks.


%package       -n ruby-railties-doc
Summary:       Documentation files for "ruby-railties" gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ruby-railties-doc
%summary


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspecdir/rails-%version.gemspec
%ruby_gemslibdir/rails-%version

%files         -n ruby-actioncable
%ruby_gemspecdir/actioncable-%version.gemspec
%ruby_gemslibdir/actioncable-%version

%files         -n ruby-actioncable-doc
%ruby_gemsdocdir/actioncable-%version

%files         -n ruby-actionmailer
%ruby_gemspecdir/actionmailer-%version.gemspec
%ruby_gemslibdir/actionmailer-%version

%files         -n ruby-actionmailer-doc
%ruby_gemsdocdir/actionmailer-%version

%files         -n ruby-actionpack
%ruby_gemspecdir/actionpack-%version.gemspec
%ruby_gemslibdir/actionpack-%version

%files         -n ruby-actionpack-doc
%ruby_gemsdocdir/actionpack-%version

%files         -n ruby-actionview
%ruby_gemspecdir/actionview-%version.gemspec
%ruby_gemslibdir/actionview-%version

%files         -n ruby-actionview-doc
%ruby_gemsdocdir/actionview-%version

%files         -n ruby-activejob
%ruby_gemspecdir/activejob-%version.gemspec
%ruby_gemslibdir/activejob-%version

%files         -n ruby-activejob-doc
%ruby_gemsdocdir/activejob-%version

%files         -n ruby-activemodel
%ruby_gemspecdir/activemodel-%version.gemspec
%ruby_gemslibdir/activemodel-%version

%files         -n ruby-activemodel-doc
%ruby_gemsdocdir/activemodel-%version

%files         -n ruby-activerecord
%ruby_gemspecdir/activerecord-%version.gemspec
%ruby_gemslibdir/activerecord-%version

%files         -n ruby-activerecord-doc
%ruby_gemsdocdir/activerecord-%version

%files         -n ruby-activestorage
%ruby_gemspecdir/activestorage-%version.gemspec
%ruby_gemslibdir/activestorage-%version

%files         -n ruby-activestorage-doc
%ruby_gemsdocdir/activestorage-%version

%files         -n ruby-activesupport
%ruby_gemspecdir/activesupport-%version.gemspec
%ruby_gemslibdir/activesupport-%version

%files         -n ruby-activesupport-doc
%ruby_gemsdocdir/activesupport-%version

%files         -n ruby-railties
%_bindir/*
%ruby_gemspecdir/railties-%version.gemspec
%ruby_gemslibdir/railties-%version

%files         -n ruby-railties-doc
%ruby_gemsdocdir/railties-%version


%changelog
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

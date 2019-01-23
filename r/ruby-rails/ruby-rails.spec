%define  pkgname rails

Name:    ruby-%pkgname
Version: 5.2.0
Release: alt1.2

Summary: Ruby on Rails
License: MIT
Group:   Development/Ruby
Url:     https://github.com/rails/rails

Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch

Source:  %pkgname-%version.tar
Source1: rails
Patch1:  %pkgname-alt-fix-path-to-bundle.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

Requires: ruby-actioncable
Requires: ruby-actionmailer
Requires: ruby-actionpack
Requires: ruby-actionview
Requires: ruby-activejob
Requires: ruby-activemodel
Requires: ruby-activerecord
Requires: ruby-activestorage
Requires: ruby-activesupport
Requires: ruby-railties

%description
Ruby on Rails (metapackage).

%package -n ruby-actioncable
Summary: WebSocket framework for Rails
Group: Development/Ruby
Requires: ruby-actionpack

%description -n ruby-actioncable
Structure many real-time application concerns into channels over a
single WebSocket connection.

%package -n ruby-actionmailer
Summary: Email composition, delivery, and receiving framework (part of Rails)
Group: Development/Ruby
Requires: ruby-actionpack ruby-actionview ruby-activejob

%description -n ruby-actionmailer
Email on Rails. Compose, deliver, receive, and test emails using the
familiar controller/view pattern. First-class support for multipart
email and attachments.

%package -n ruby-actionpack
Summary: Web-flow and rendering framework putting the VC in MVC (part of Rails)
Group: Development/Ruby
Requires: ruby-activesupport

%description -n ruby-actionpack
Web apps on Rails. Simple, battle-tested conventions for building and
testing MVC web applications. Works with any Rack-compatible server.

%package -n ruby-actionview
Summary: Rendering framework putting the V in MVC (part of Rails)
Group: Development/Ruby
Requires: ruby-activesupport

%description -n ruby-actionview
Simple, battle-tested conventions and helpers for building web pages.

%package -n ruby-activejob
Summary: Job framework with pluggable queues
Group: Development/Ruby
Requires: ruby-activesupport

%description -n ruby-activejob
Declare job classes that can be run by a variety of queueing backends.

%package -n ruby-activemodel
Summary: A toolkit for building modeling frameworks (part of Rails)
Group: Development/Ruby
Requires: ruby-activesupport

%description -n ruby-activemodel
A toolkit for building modeling frameworks like Active Record. Rich
support for attributes, callbacks, validations, serialization,
internationalization, and testing.

%package -n ruby-activerecord
Summary: Object-relational mapper framework (part of Rails)
Group: Development/Ruby
Requires: ruby-activesupport ruby-activemodel
Provides: activerecord-gems = %EVR
Obsoletes: activerecord-gems < %EVR

%description -n ruby-activerecord
Databases on Rails. Build a persistent domain model by mapping database
tables to Ruby classes. Strong conventions for associations,
validations, aggregations, migrations, and testing come baked-in.

%package -n ruby-activestorage
Summary: Local and cloud file storage framework
Group: Development/Ruby
Requires: ruby-activesupport ruby-actionpack

%description -n ruby-activestorage
Attach cloud and local files in Rails applications.

%package -n ruby-activesupport
Summary: A toolkit of support libraries and Ruby core extensions extracted from the Rails framework
Group: Development/Ruby
Provides: activesupport-gems = %EVR
Obsoletes: activesupport-gems < %EVR

%description -n ruby-activesupport
A toolkit of support libraries and Ruby core extensions extracted from
the Rails framework. Rich support for multibyte strings,
internationalization, time zones, and testing.

%package -n ruby-railties
Summary: Tools for creating, working with, and running Rails applications
Group: Development/Ruby
Requires: ruby-activesupport ruby-actionpack

%description -n ruby-railties
Rails internals: application bootup, plugins, generators, and rake tasks.

%package doc
Summary: Documentation files for %name
Group: Documentation
Provides: activerecord-gems-doc = %EVR
Obsoletes: activerecord-gems-doc < %EVR
Provides: activesupport-gems-doc = %EVR
Obsoletes: activesupport-gems-doc < %EVR

BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%patch1 -p1
for dir in . actioncable actionmailer actionpack actionview activejob activemodel activerecord activestorage activesupport railties;do
	pushd $dir
	%update_setup_rb
	popd
done

%build
for dir in . actioncable actionmailer actionpack actionview activejob activemodel activerecord activestorage activesupport railties;do
	pushd $dir
	%ruby_config
	%ruby_build
	popd
done

%install
for dir in . actioncable actionmailer actionpack actionview activejob activemodel activerecord activestorage activesupport railties;do
	pushd $dir
	%ruby_install
	popd
done
rm -rf %buildroot%_bindir/*
install -Dm0755 %SOURCE1 %buildroot%_bindir/rails
#%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test_unit -Ilib:test test

%files
%doc README*
%rubygem_specdir/rails*

%files -n ruby-actioncable
%ruby_sitelibdir/action_cable*
%ruby_sitelibdir/rails/generators/channel
%rubygem_specdir/actioncable*

%files -n ruby-actionmailer
%ruby_sitelibdir/action_mailer*
%ruby_sitelibdir/rails/generators/mailer
%rubygem_specdir/actionmailer*

%files -n ruby-actionpack
%ruby_sitelibdir/abstract_controller*
%ruby_sitelibdir/action_controller*
%ruby_sitelibdir/action_dispatch*
%ruby_sitelibdir/action_pack*
%rubygem_specdir/actionpack*

%files -n ruby-actionview
%ruby_sitelibdir/action_view*
%rubygem_specdir/actionview*

%files -n ruby-activejob
%ruby_sitelibdir/active_job*
%ruby_sitelibdir/rails/generators/job
%rubygem_specdir/activejob*

%files -n ruby-activemodel
%ruby_sitelibdir/active_model*
%rubygem_specdir/activemodel*

%files -n ruby-activerecord
%ruby_sitelibdir/active_record*
%ruby_sitelibdir/rails/generators/active_record*
%rubygem_specdir/activerecord*

%files -n ruby-activestorage
%ruby_sitelibdir/active_storage*
%ruby_sitelibdir/tasks/activestorage.rake
%rubygem_specdir/activestorage*

%files -n ruby-activesupport
%ruby_sitelibdir/active_support*
%rubygem_specdir/activesupport*

%files -n ruby-railties
%_bindir/rails
%ruby_sitelibdir/rails*
%ruby_sitelibdir/minitest/rails_plugin.rb
%exclude %ruby_sitelibdir/rails/generators/channel
%exclude %ruby_sitelibdir/rails/generators/mailer
%exclude %ruby_sitelibdir/rails/generators/job
%exclude %ruby_sitelibdir/rails/generators/active_record*
%rubygem_specdir/railties*

%files doc
#%ruby_ri_sitedir/*

%changelog
* Wed Jan 23 2019 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1.2
- Remove deprecated macros.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- Initial build for Sisyphus

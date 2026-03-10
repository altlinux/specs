%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname katello

Name:          gem-katello
Version:       4.19.0.1
Release:       alt1
Summary:       Content and Subscription Management plugin for Foreman
License:       GPL-2.0 or GPL-2.0-or-later
Group:         Development/Ruby
Url:           http://www.katello.org
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         pulp.patch
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activerecord-import) >= 0
BuildRequires: gem(angular-rails-templates) >= 1.1
BuildRequires: gem(apipie-rails) >= 0.5.14
BuildRequires: gem(deface) >= 1.0.2
BuildRequires: gem(dynflow) >= 1.6.1
BuildRequires: gem(faraday) >= 1.10.2
BuildRequires: gem(foreman-tasks) >= 9.1.0
BuildRequires: gem(foreman_remote_execution) >= 7.1.0
BuildRequires: gem(jquery-ui-rails) >= 7.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(oauth) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(rabl) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(scoped_search) >= 4.1.9
BuildRequires: gem(spidr) >= 0
BuildRequires: gem(stomp) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildRequires: gem(vcr) >= 6.1
BuildConflicts: gem(angular-rails-templates) >= 2
BuildConflicts: gem(deface) >= 2.0.0
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(fx) >= 1.0
BuildConflicts: gem(jquery-ui-rails) >= 8
BuildConflicts: gem(theforeman-rubocop) >= 1
BuildConflicts: gem(vcr) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency theforeman-rubocop >= 0.1.2,theforeman-rubocop < 1
%ruby_use_gem_dependency jquery-ui-rails >= 7.0,jquery-ui-rails < 8
Requires:      ruby >= 3.0
Requires:      gem(activerecord-import) >= 0
Requires:      gem(angular-rails-templates) >= 1.1
Requires:      gem(apipie-rails) >= 0.5.14
Requires:      gem(deface) >= 1.0.2
Requires:      gem(dynflow) >= 1.6.1
Requires:      gem(faraday) >= 1.10.2
Requires:      gem(foreman-tasks) >= 9.1.0
Requires:      gem(foreman_remote_execution) >= 7.1.0
Requires:      gem(jquery-ui-rails) >= 7.0
Requires:      gem(json) >= 0
Requires:      gem(oauth) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(rabl) >= 0
Requires:      gem(rails) >= 0
Requires:      gem(rest-client) >= 0
Requires:      gem(scoped_search) >= 4.1.9
Requires:      gem(spidr) >= 0
Requires:      gem(stomp) >= 0
Conflicts:     ruby >= 4
Conflicts:     gem(angular-rails-templates) >= 2
Conflicts:     gem(deface) >= 2.0.0
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(fx) >= 1.0
Conflicts:     gem(jquery-ui-rails) >= 8
Provides:      gem(katello) = 4.19.0.1

%description
Katello adds Content and Subscription Management to Foreman. For this it relies
on Candlepin and Pulp.


%package       -n gem-bastion
Version:       6.1.22
Release:       alt1
Summary:       Bastion UI library of AngularJS
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Provides:      gem(bastion) = 6.1.22

%description   -n gem-bastion
Bastion provides a UI library of AngularJS based components designed to
integrate and work with Foreman

Katello adds Content and Subscription Management to Foreman. For this it relies
on Candlepin and Pulp.


%if_enabled    doc
%package       -n gem-bastion-doc
Version:       6.1.22
Release:       alt1
Summary:       Bastion UI library of AngularJS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bastion
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(bastion) = 6.1.22

%description   -n gem-bastion-doc
Bastion UI library of AngularJS documentation files.

Bastion provides a UI library of AngularJS based components designed to
integrate and work with Foreman

Katello adds Content and Subscription Management to Foreman. For this it relies
on Candlepin and Pulp.

%description   -n gem-bastion-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bastion.
%endif


%if_enabled    doc
%package       -n gem-katello-doc
Version:       4.19.0.1
Release:       alt1
Summary:       Content and Subscription Management plugin for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета katello
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(katello) = 4.19.0.1

%description   -n gem-katello-doc
Content and Subscription Management plugin for Foreman documentation
files.

Katello adds Content and Subscription Management to Foreman. For this it relies
on Candlepin and Pulp.

%description   -n gem-katello-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета katello.
%endif


%if_enabled    devel
%package       -n gem-katello-devel
Version:       4.19.0.1
Release:       alt1
Summary:       Content and Subscription Management plugin for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета katello
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(katello) = 4.19.0.1
Requires:      gem(theforeman-rubocop) >= 0.1.0
Requires:      gem(vcr) >= 6.1
Conflicts:     gem(theforeman-rubocop) >= 1
Conflicts:     gem(vcr) >= 7

%description   -n gem-katello-devel
Content and Subscription Management plugin for Foreman development
package.

Katello adds Content and Subscription Management to Foreman. For this it relies
on Candlepin and Pulp.

%description   -n gem-katello-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета katello.
%endif


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
%doc LICENSE.txt README.md CONTRIBUTORS
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-bastion
%doc CHANGELOG.md README.md
%ruby_gemspecdir/bastion-6.1.22.gemspec
%ruby_gemslibdir/bastion-6.1.22

%if_enabled    doc
%files         -n gem-bastion-doc
%doc CHANGELOG.md README.md
%ruby_gemsdocdir/bastion-6.1.22
%endif

%if_enabled    doc
%files         -n gem-katello-doc
%doc LICENSE.txt README.md CONTRIBUTORS
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-katello-devel
%doc LICENSE.txt README.md CONTRIBUTORS
%endif


%changelog
* Tue Mar 10 2026 Pavel Skrylev <majioa@altlinux.org> 4.19.0.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

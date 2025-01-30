%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          gem-zeus
Version:       0.17.0
Release:       alt1
Summary:       Zeus is an intelligent preloader for ruby applications
License:       MIT
Group:         Development/Ruby
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gcc-c++
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ronn-ng) >= 0
BuildConflicts: gem(bundler) >= 3
%if_enabled check
BuildRequires: gem(method_source) >= 0.6.7
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rspec) >= 3.1
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names gem-zeus
Requires:      gem(method_source) >= 0.6.7

%ruby_use_gem_version vagrant-zeus:0.17.0
%ruby_use_gem_version zeus:0.17.0

%description
Zeus is an intelligent preloader for ruby applications. It allows normal
development tasks to be run in a fraction of a second. Boot any rails app in
under a second.

Zeus preloads your Rails app so that your normal development tasks such as
console, server, generate, and specs/tests take less than one second.

This screencast gives a quick overview of how to use zeus with Rails.


%package       -n gem-vagrant-zeus
Version:       0.17.0
Release:       alt1
Summary:       This plugin watches for filesystem events
Group:         Development/Ruby

Requires:      gem(method_source) >= 0.6.7
Requires:      gem(zeus) >= 0
Provides:      gem(vagrant-zeus) = 0.17.0

%description   -n gem-vagrant-zeus
This plugin watches for filesystem events.

This plugin watches for filesystem events on the local filesystem, and sends
them over a network socket to Zeus listening from inside the VM. Vagrant plugin
to pass along filesystem events on directories shared with the VM

%package       -n zeus
Version:       0.17.0
Release:       alt1
Summary:       Zeus is an intelligent preloader for ruby applications executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета zeus
Group:         Other
BuildArch:     noarch

Requires:      gem(zeus) = 0.17.0

%description   -n zeus
Zeus is an intelligent preloader for ruby applications executable(s).

Boot any rails app in under a second

%description   -n zeus -l ru_RU.UTF-8
Исполнямка для самоцвета zeus.


%if_enabled    doc
%package       -n gem-zeus-doc
Version:       0.17.0
Release:       alt1
Summary:       Zeus is an intelligent preloader for ruby applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zeus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zeus) = 0.17.0

%description   -n gem-zeus-doc
Zeus is an intelligent preloader for ruby applications documentation files.

Boot any rails app in under a second

%description   -n gem-zeus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zeus.
%endif


%if_enabled    devel
%package       -n gem-zeus-devel
Version:       0.17.0
Release:       alt1
Summary:       Zeus is an intelligent preloader for ruby applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета zeus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(zeus) = 0.17.0
Requires:      gem(bundler) >= 2.3
Requires:      gem(method_source) >= 0.6.7
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 0
Requires:      gem(ronn-ng) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(zeus) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rspec) >= 4

%description   -n gem-zeus-devel
Zeus is an intelligent preloader for ruby applications development package.

Boot any rails app in under a second

%description   -n gem-zeus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета zeus.
%endif


%if_enabled    doc
%package       -n gem-vagrant-zeus-doc
Version:       0.17.0
Release:       alt1
Summary:       This plugin watches for filesystem events documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vagrant-zeus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vagrant-zeus) = 0.17.0

%description   -n gem-vagrant-zeus-doc
This plugin watches for filesystem events documentation files.

This plugin watches for filesystem events on the local filesystem, and sends
them over a network socket to Zeus listening from inside the VM. Vagrant plugin
to pass along filesystem events on directories shared with the VM

%description   -n gem-vagrant-zeus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vagrant-zeus.
%endif


%if_enabled    devel
%package       -n gem-vagrant-zeus-devel
Version:       0.17.0
Release:       alt1
Summary:       This plugin watches for filesystem events development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vagrant-zeus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vagrant-zeus) = 0.17.0
Requires:      gem(bundler) >= 2.3
Requires:      gem(method_source) >= 0.6.7
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 0
Requires:      gem(ronn-ng) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(zeus) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rspec) >= 4

%description   -n gem-vagrant-zeus-devel
This plugin watches for filesystem events development package.

This plugin watches for filesystem events on the local filesystem, and sends
them over a network socket to Zeus listening from inside the VM. Vagrant plugin
to pass along filesystem events on directories shared with the VM

%description   -n gem-vagrant-zeus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vagrant-zeus.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc MIT-LICENSE
%ruby_gemspecdir/zeus-0.17.0.gemspec
%ruby_gemslibdir/zeus-0.17.0

%files         -n gem-vagrant-zeus
%doc MIT-LICENSE
%ruby_gemspecdir/vagrant-zeus-0.17.0.gemspec
%ruby_gemslibdir/vagrant-zeus-0.17.0
%ruby_gemsextdir/vagrant-zeus-0.17.0

%files         -n zeus
%doc MIT-LICENSE
%_bindir/zeus

%if_enabled    doc
%files         -n gem-zeus-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/zeus-0.17.0
%endif

%if_enabled    devel
%files         -n gem-zeus-devel
%doc MIT-LICENSE
%endif

%if_enabled    doc
%files         -n gem-vagrant-zeus-doc
%doc MIT-LICENSE
%ruby_gemsdocdir/vagrant-zeus-0.17.0
%endif

%if_enabled    devel
%files         -n gem-vagrant-zeus-devel
%doc MIT-LICENSE
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- + packaged gem with Ruby Policy 2.0

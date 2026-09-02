%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-mock

Name:          gem-minitest-mock
Version:       5.27.0
Release:       alt1
Summary:       minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object framework
License:       MIT
Group:         Development/Ruby
Url:           https://minite.st/
Vcs:           https://github.com/minitest/minitest-mock.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(hoe) >= 4.2
BuildRequires: gem(hoe-git2) > 0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0
Requires:      ruby >= 3.2
Provides:      gem(minitest-mock) = 5.27.0

%description
minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object
framework.

The minitest-mock gem is an extraction of minitest/mock.rb from minitest in
order to make it easier to maintain independent of minitest.


%if_enabled    doc
%package       -n gem-minitest-mock-doc
Version:       5.27.0
Release:       alt1
Summary:       minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-mock
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-mock) = 5.27.0

%description   -n gem-minitest-mock-doc
minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object
framework documentation files.

%description   -n gem-minitest-mock-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-mock.
%endif


%if_enabled    devel
%package       -n gem-minitest-mock-devel
Version:       5.27.0
Release:       alt1
Summary:       minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-mock
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-mock) = 5.27.0
Requires:      gem(hoe) >= 4.2
Requires:      gem(hoe-git2) > 0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(rdoc) >= 7

%description   -n gem-minitest-mock-devel
minitest/mock, by Steven Baker, is a beautifully tiny mock (and stub) object
framework development package.

%description   -n gem-minitest-mock-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-mock.
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
%doc History.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-mock-doc
%doc History.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-mock-devel
%doc History.rdoc README.rdoc
%endif


%changelog
* Sun May 31 2026 Pavel Skrylev <majioa@altlinux.org> 5.27.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

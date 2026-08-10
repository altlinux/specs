%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ostruct

Name:          gem-ostruct
Version:       0.6.3
Release:       alt1
Summary:       Class to build custom data structures, similar to a Hash
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/ostruct
Vcs:           https://github.com/ruby/ostruct.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Provides:      gem(ostruct) = 0.6.3

%description
Class to build custom data structures, similar to a Hash.


%if_enabled    doc
%package       -n gem-ostruct-doc
Version:       0.6.3
Release:       alt1
Summary:       Class to build custom data structures, similar to a Hash documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ostruct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ostruct) = 0.6.3

%description   -n gem-ostruct-doc
Class to build custom data structures, similar to a Hash documentation files.

%description   -n gem-ostruct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ostruct.
%endif


%if_enabled    devel
%package       -n gem-ostruct-devel
Version:       0.6.3
Release:       alt1
Summary:       Class to build custom data structures, similar to a Hash development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ostruct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ostruct) = 0.6.3
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-ostruct-devel
Class to build custom data structures, similar to a Hash development package.

%description   -n gem-ostruct-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ostruct.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ostruct-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ostruct-devel
%doc COPYING README.md
%endif


%changelog
* Mon Aug 10 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

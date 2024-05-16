%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname reline

Name:          gem-reline
Version:       0.5.1
Release:       alt1
Summary:       Alternative GNU Readline or Editline implementation by pure Ruby
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/reline
Vcs:           https://github.com/ruby/reline.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(io-console) >= 0.5
BuildConflicts: gem(io-console) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(io-console) >= 0.5
Conflicts:     gem(io-console) >= 1
Provides:      gem(reline) = 0.5.1


%description
Alternative GNU Readline or Editline implementation by pure Ruby.


%if_enabled    doc
%package       -n gem-reline-doc
Version:       0.5.1
Release:       alt1
Summary:       Alternative GNU Readline or Editline implementation by pure Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета reline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(reline) = 0.5.1

%description   -n gem-reline-doc
Alternative GNU Readline or Editline implementation by pure Ruby documentation
files.

%description   -n gem-reline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета reline.
%endif


%if_enabled    devel
%package       -n gem-reline-devel
Version:       0.5.1
Release:       alt1
Summary:       Alternative GNU Readline or Editline implementation by pure Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета reline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(reline) = 0.5.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-reline-devel
Alternative GNU Readline or Editline implementation by pure Ruby development
package.

%description   -n gem-reline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета reline.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-reline-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-reline-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- ^ 0.3.1 -> 0.5.1

* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- + packaged gem with Ruby Policy 2.0

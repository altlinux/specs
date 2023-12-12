# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        gemname foreman

Name:          gem-foreman
Version:       0.87.2
Release:       alt1
Summary:       Process manager for applications with multiple components
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ddollar/foreman
Vcs:           https://github.com/ddollar/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(thor) >= 1.2.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(fakefs) >= 0.10.0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(aws-s3) >= 0
BuildRequires: gem(ronn) >= 0
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(automatiek) >= 0
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(fakefs) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency thor >= 1.2.1,thor < 2
%ruby_use_gem_dependency fakefs >= 1.9.0,fakefs < 2
Provides:      gem(foreman) = 0.87.2

%ruby_bindir_to %ruby_bindir

%description
Process manager for applications with multiple components.


%package       -n foreman-rb
Version:       0.87.2
Release:       alt1
Summary:       Process manager for applications with multiple components executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета foreman
Group:         Other
BuildArch:     noarch

Requires:      gem(foreman) = 0.87.2

%description   -n foreman-rb
Process manager for applications with multiple components executable(s).

%description   -n foreman-rb -l ru_RU.UTF-8
Исполнямка для самоцвета foreman.


%package       -n gem-foreman-doc
Version:       0.87.2
Release:       alt1
Summary:       Process manager for applications with multiple components documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman) = 0.87.2

%description   -n gem-foreman-doc
Process manager for applications with multiple components documentation files.

%description   -n gem-foreman-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman.


%package       -n gem-foreman-devel
Version:       0.87.2
Release:       alt1
Summary:       Process manager for applications with multiple components development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman) = 0.87.2
Requires:      gem(thor) >= 1.2.1
Requires:      gem(rake) >= 0
Requires:      gem(fakefs) >= 0.10.0
Requires:      gem(rspec) >= 3.5
Requires:      gem(simplecov) >= 0
Requires:      gem(timecop) >= 0
Requires:      gem(codeclimate-test-reporter) >= 0
Requires:      gem(aws-s3) >= 0
Requires:      gem(ronn) >= 0
Requires:      gem(yard) >= 0.9.11
Requires:      gem(automatiek) >= 0
Conflicts:     gem(thor) >= 2
Conflicts:     gem(fakefs) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-foreman-devel
Process manager for applications with multiple components development package.

%description   -n gem-foreman-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman.


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

%files         -n foreman-rb
%doc README.md
%ruby_bindir/foreman
%ruby_mandir/foreman.1.xz

%files         -n gem-foreman-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.87.2-alt1
- ^ 0.87.0 -> 0.87.2

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 0.87.0-alt1
- + packaged gem with usage Ruby Policy 2.0

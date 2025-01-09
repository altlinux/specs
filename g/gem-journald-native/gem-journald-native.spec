# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname journald-native

Name:          gem-journald-native
Version:       1.0.12
Release:       alt1
Summary:       systemd-journal logging interface wrapper for ruby
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           https://github.com/theforeman/journald-native
Vcs:           https://github.com/theforeman/journald-native.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libsystemd-devel
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildConflicts: gem(bundler) >= 3
%if_enabled check
BuildRequires: gem(rspec) >= 3.4
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 1.9.3
Provides:      gem(journald-native) = 1.0.12

%description
A systemd-journal native logging lib wrapper.


%if_enabled    doc
%package       -n gem-journald-native-doc
Version:       1.0.12
Release:       alt1
Summary:       systemd-journal logging interface wrapper for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета journald-native
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(journald-native) = 1.0.12

%description   -n gem-journald-native-doc
systemd-journal logging interface wrapper for ruby documentation files.

A systemd-journal native logging lib wrapper.

%description   -n gem-journald-native-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета journald-native.
%endif


%if_enabled    devel
%package       -n gem-journald-native-devel
Version:       1.0.12
Release:       alt1
Summary:       systemd-journal logging interface wrapper for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета journald-native
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libsystemd-devel
Requires:      gem(journald-native) = 1.0.12
Requires:      gem(bundler) >= 1.6
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rspec) >= 3.4
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-journald-native-devel
systemd-journal logging interface wrapper for ruby development package.

A systemd-journal native logging lib wrapper.

%description   -n gem-journald-native-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета journald-native.
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
%doc CHANGELOG.md COPYING.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-journald-native-doc
%doc CHANGELOG.md COPYING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-journald-native-devel
%doc CHANGELOG.md COPYING.md README.md
%ruby_includedir/*
%endif


%changelog
* Thu Jan 09 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.12-alt1
- ^ 1.0.11 -> 1.0.12
- * define explicit dependencies

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1.3
- ! spec tag

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1.1
- fixed (!) spec according to changelog rules

* Wed Aug 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.11-alt1
- + packaged gem with usage Ruby Policy 2.0

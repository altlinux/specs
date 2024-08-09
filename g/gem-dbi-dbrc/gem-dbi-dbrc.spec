%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dbi-dbrc

Name:          gem-dbi-dbrc
Version:       1.7.0.24
Release:       alt0.1
Summary:       A simple way to avoid hard-coding passwords with DBI
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/djberg96/dbi-dbrc
Vcs:           https://github.com/djberg96/dbi-dbrc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(fakefs) >= 1.3
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(gpgme) >= 2.0.21
BuildRequires: gem(rexml) >= 3.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(fakefs) >= 3
BuildConflicts: gem(gpgme) >= 2.1
BuildConflicts: gem(rexml) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency fakefs >= 2.5.0,fakefs < 3
Requires:      gem(gpgme) >= 2.0.21
Requires:      gem(rexml) >= 3.2
Conflicts:     gem(gpgme) >= 2.1
Conflicts:     gem(rexml) >= 4
Provides:      gem(dbi-dbrc) = 1.7.0.24

%ruby_use_gem_version dbi-dbrc:1.7.0.24

%description
The dbi-dbrc library provides an interface for storing database connection
information, including passwords, in a locally secure file only accessible by
you, or root. This allows you to avoid hard coding login and password
information in your programs that require such information.

This library can also be used to store login and password information for logins
on remote hosts, not just databases.


%if_enabled    doc
%package       -n gem-dbi-dbrc-doc
Version:       1.7.0.24
Release:       alt0.1
Summary:       A simple way to avoid hard-coding passwords with DBI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dbi-dbrc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dbi-dbrc) = 1.7.0.24

%description   -n gem-dbi-dbrc-doc
A simple way to avoid hard-coding passwords with DBI documentation files.

The dbi-dbrc library provides an interface for storing database connection
information, including passwords, in a locally secure file only accessible by
you, or root. This allows you to avoid hard coding login and password
information in your programs that require such information.

This library can also be used to store login and password information for logins
on remote hosts, not just databases.

%description   -n gem-dbi-dbrc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dbi-dbrc.
%endif


%if_enabled    devel
%package       -n gem-dbi-dbrc-devel
Version:       1.7.0.24
Release:       alt0.1
Summary:       A simple way to avoid hard-coding passwords with DBI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dbi-dbrc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dbi-dbrc) = 1.7.0.24
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.9
Requires:      gem(fakefs) >= 1.3
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-rspec) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(fakefs) >= 3

%description   -n gem-dbi-dbrc-devel
A simple way to avoid hard-coding passwords with DBI development package.

The dbi-dbrc library provides an interface for storing database connection
information, including passwords, in a locally secure file only accessible by
you, or root. This allows you to avoid hard coding login and password
information in your programs that require such information.

This library can also be used to store login and password information for logins
on remote hosts, not just databases.

%description   -n gem-dbi-dbrc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dbi-dbrc.
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
%files         -n gem-dbi-dbrc-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dbi-dbrc-devel
%doc README.md
%endif


%changelog
* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.0.24-alt0.1
- ^ 1.7.0 -> 1.7.0p24

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with Ruby Policy 2.0

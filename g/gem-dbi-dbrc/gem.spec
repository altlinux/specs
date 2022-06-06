%define        gemname dbi-dbrc

Name:          gem-dbi-dbrc
Version:       1.7.0
Release:       alt1
Summary:       A simple way to avoid hard-coding passwords with DBI
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/djberg96/dbi-dbrc
Vcs:           https://github.com/djberg96/dbi-dbrc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gpgme) >= 2.0 gem(gpgme) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(fakefs) >= 1.3 gem(fakefs) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(gpgme) >= 2.0 gem(gpgme) < 3
Provides:      gem(dbi-dbrc) = 1.7.0


%description
The dbi-dbrc library provides an interface for storing database connection
information, including passwords, in a locally secure file only accessible by
you, or root. This allows you to avoid hard coding login and password
information in your programs that require such information.

This library can also be used to store login and password information for logins
on remote hosts, not just databases.


%package       -n gem-dbi-dbrc-doc
Version:       1.7.0
Release:       alt1
Summary:       A simple way to avoid hard-coding passwords with DBI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dbi-dbrc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dbi-dbrc) = 1.7.0

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


%package       -n gem-dbi-dbrc-devel
Version:       1.7.0
Release:       alt1
Summary:       A simple way to avoid hard-coding passwords with DBI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dbi-dbrc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dbi-dbrc) = 1.7.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(fakefs) >= 1.3 gem(fakefs) < 2

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

%files         -n gem-dbi-dbrc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-dbi-dbrc-devel
%doc README.md


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with Ruby Policy 2.0

%define        gemname zonefile

Name:          gem-zonefile
Version:       1.07
Release:       alt1
Summary:       BIND Zonefile Reader and Writer
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/boesemar/zonefile
Vcs:           https://github.com/boesemar/zonefile.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(zonefile) = 1.07


%description
A library that can create, read, write, modify BIND compatible Zonefiles
(RFC1035). Warning: It probably works for most cases, but it might not be able
to read all files even if they are valid for bind.


%package       -n gem-zonefile-doc
Version:       1.07
Release:       alt1
Summary:       BIND Zonefile Reader and Writer documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zonefile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zonefile) = 1.07

%description   -n gem-zonefile-doc
BIND Zonefile Reader and Writer documentation files.

A library that can create, read, write, modify BIND compatible Zonefiles
(RFC1035). Warning: It probably works for most cases, but it might not be able
to read all files even if they are valid for bind.

%description   -n gem-zonefile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zonefile.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-zonefile-doc
%ruby_gemdocdir


%changelog
* Fri Jun 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.07-alt1
- + packaged gem with Ruby Policy 2.0

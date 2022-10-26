%define        gemname rmail

Name:          gem-rmail
Version:       1.1.4
Release:       alt1
Summary:       A MIME mail parsing and generation library
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/terceiro/rmail
Vcs:           https://github.com/terceiro/rmail.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rmail) = 1.1.4


%description
RMail is a lightweight mail library containing various utility classes and
modules that allow ruby scripts to parse, modify, and generate MIME mail
messages.


%package       -n gem-rmail-doc
Version:       1.1.4
Release:       alt1
Summary:       A MIME mail parsing and generation library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rmail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rmail) = 1.1.4

%description   -n gem-rmail-doc
A MIME mail parsing and generation library documentation files.

RMail is a lightweight mail library containing various utility classes and
modules that allow ruby scripts to parse, modify, and generate MIME mail
messages.

%description   -n gem-rmail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rmail.


%package       -n gem-rmail-devel
Version:       1.1.4
Release:       alt1
Summary:       A MIME mail parsing and generation library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rmail
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rmail) = 1.1.4
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(coveralls) >= 0

%description   -n gem-rmail-devel
A MIME mail parsing and generation library development package.

RMail is a lightweight mail library containing various utility classes and
modules that allow ruby scripts to parse, modify, and generate MIME mail
messages.

%description   -n gem-rmail-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rmail.


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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rmail-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rmail-devel
%doc README.md


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- + packaged gem with Ruby Policy 2.0

%define        gemname unicode-version

Name:          gem-unicode-version
Version:       1.2.0
Release:       alt1
Summary:       Ruby / Unicode / Emoji versions mapping
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/unicode-version
Vcs:           https://github.com/janlelis/unicode-version.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(unicode-version) = 1.2.0


%description
Returns Unicode / Emoji versions of current and previous Rubies.


%package       -n gem-unicode-version-doc
Version:       1.2.0
Release:       alt1
Summary:       Ruby / Unicode / Emoji versions mapping documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unicode-version
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unicode-version) = 1.2.0

%description   -n gem-unicode-version-doc
Ruby / Unicode / Emoji versions mapping documentation files.

Returns Unicode / Emoji versions of current and previous Rubies.

%description   -n gem-unicode-version-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unicode-version.


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

%files         -n gem-unicode-version-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0

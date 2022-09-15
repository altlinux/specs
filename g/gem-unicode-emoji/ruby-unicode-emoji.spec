%define        gemname unicode-emoji

Name:          gem-unicode-emoji
Version:       3.1.0
Release:       alt1
Summary:       Emoji Regex in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/janlelis/unicode-emoji
Vcs:           https://github.com/janlelis/unicode-emoji.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(unicode-version) >= 1.0 gem(unicode-version) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(unicode-version) >= 1.0 gem(unicode-version) < 2
Obsoletes:     ruby-unicode-emoji < %EVR
Provides:      ruby-unicode-emoji = %EVR
Provides:      gem(unicode-emoji) = 3.1.0


%description
A small Ruby library which provides Unicode Emoji data and regexes. Also
includes a categorized list of recommended Emoji.


%package       -n gem-unicode-emoji-doc
Version:       3.1.0
Release:       alt1
Summary:       Emoji Regex in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unicode-emoji
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unicode-emoji) = 3.1.0

%description   -n gem-unicode-emoji-doc
Emoji Regex in Ruby documentation files.

A small Ruby library which provides Unicode Emoji data and regexes. Also
includes a categorized list of recommended Emoji.

%description   -n gem-unicode-emoji-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unicode-emoji.


%package       -n gem-unicode-emoji-devel
Version:       3.1.0
Release:       alt1
Summary:       Emoji Regex in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unicode-emoji
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unicode-emoji) = 3.1.0

%description   -n gem-unicode-emoji-devel
Emoji Regex in Ruby development package.

A small Ruby library which provides Unicode Emoji data and regexes. Also
includes a categorized list of recommended Emoji.

%description   -n gem-unicode-emoji-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unicode-emoji.


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

%files         -n gem-unicode-emoji-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-unicode-emoji-devel
%doc README.md


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 2.4.0 -> 3.1.0

* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- updated ^ 2.1.0 -> 2.4.0
- fixed ! spec

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.1.0 -> 2.1.0
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

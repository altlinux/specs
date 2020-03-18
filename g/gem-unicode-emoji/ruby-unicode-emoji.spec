# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname unicode-emoji

Name:          gem-%pkgname
Version:       2.4.0
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
A small Ruby library which provides Unicode Emoji data and regexes.
Also includes a categorized list of recommended Emoji.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
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

%define        pkgname twitter-text

Name:          %pkgname
Version:       3.0.1
Release:       alt1
Summary:       Twitter Text Libraries
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/twitter/twitter-text
%vcs           https://github.com/twitter/twitter-text.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
Requires:      gem-%pkgname = %version

%description
This repo is a collection of libraries and conformance tests to standardize
parsing of Tweet text. It synchronizes development, testing, creating issues,
and pull requests for twitter-text's implementations and specification. These
libraries are responsible for determining the quantity of characters in a Tweet
and identifying and linking any url, @username, #hashtag, or $cashtag.


%package       -n gem-%pkgname
Summary:       A gem that provides text handling for Twitter
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
%summary. Library files for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
%summary. Библиотеки для %gemname самоцвета.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version --ignore=conformance

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-%pkgname
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

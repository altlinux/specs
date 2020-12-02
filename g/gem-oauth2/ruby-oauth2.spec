%define        pkgname oauth2

Name:          gem-%pkgname
Version:       1.4.4
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oauth-xx/oauth2
Vcs:           https://github.com/oauth-xx/oauth2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.


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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1
- > Ruby Policy 2.0
- ^ 1.4.1 -> 1.4.4

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus

%define        gemname libyajl2

Name:          gem-libyajl2
Version:       2.1.0
Release:       alt1
Summary:       gem to install the libyajl2 c-library for distributions which do not have it
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/libyajl2-gem
Vcs:           https://github.com/chef/libyajl2-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(libyajl2) = 2.1.0


%description
gem to install the libyajl2 c-library for distributions which do not have it.


%package       -n gem-libyajl2-doc
Version:       2.1.0
Release:       alt1
Summary:       gem to install the libyajl2 c-library for distributions which do not have it documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета libyajl2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(libyajl2) = 2.1.0

%description   -n gem-libyajl2-doc
gem to install the libyajl2 c-library for distributions which do not have it
documentation files.

%description   -n gem-libyajl2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета libyajl2.


%prep
%setup

%build
%ruby_build --mode=flex

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-libyajl2-doc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.2.0 -> 2.1.0

* Tue Feb 05 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Initial build to ALT of 1.2.0 with usage of Ruby Policy 2.0.

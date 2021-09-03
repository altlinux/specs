%define        gemname ntlm-http

Name:          gem-ntlm-http
Version:       0.1.3.3
Release:       alt1.1
Summary:       Ruby/NTLM HTTP library
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/pyu10055/ntlm-http
Vcs:           https://github.com/pyu10055/ntlm-http.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ntlm-http) = 0.1.3.3


%description
Ruby/NTLM HTTP provides NTLM authentication over http.


%package       -n gem-pyu-ntlm-http
Version:       0.1.3.2
Release:       alt1.1
Summary:       Ruby/NTLM HTTP library
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(pyu-ntlm-http) = 0.1.3.2

%description   -n gem-pyu-ntlm-http
Ruby/NTLM HTTP provides NTLM authentication over http.


%package       -n gem-pyu-ntlm-http-doc
Version:       0.1.3.2
Release:       alt1.1
Summary:       Ruby/NTLM HTTP library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pyu-ntlm-http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pyu-ntlm-http) = 0.1.3.2

%description   -n gem-pyu-ntlm-http-doc
Ruby/NTLM HTTP library documentation files.

Ruby/NTLM HTTP provides NTLM authentication over http.

%description   -n gem-pyu-ntlm-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pyu-ntlm-http.


%package       -n gem-ntlm-http-doc
Version:       0.1.3.3
Release:       alt1.1
Summary:       Ruby/NTLM HTTP library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ntlm-http
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ntlm-http) = 0.1.3.3

%description   -n gem-ntlm-http-doc
Ruby/NTLM HTTP library documentation files.

Ruby/NTLM HTTP provides NTLM authentication over http.

%description   -n gem-ntlm-http-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ntlm-http.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-pyu-ntlm-http
%doc README
%ruby_gemspecdir/pyu-ntlm-http-0.1.3.2.gemspec
%ruby_gemslibdir/pyu-ntlm-http-0.1.3.2

%files         -n gem-pyu-ntlm-http-doc
%doc README
%ruby_gemsdocdir/pyu-ntlm-http-0.1.3.2

%files         -n gem-ntlm-http-doc
%doc README
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.3.3-alt1.1
- ! spec

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.3.3-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

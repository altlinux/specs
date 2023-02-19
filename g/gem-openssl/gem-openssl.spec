%define        gemname openssl

Name:          gem-openssl
Version:       3.1.0
Release:       alt1
Summary:       It wraps the OpenSSL library
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/ruby/openssl
Vcs:           https://github.com/ruby/openssl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 3.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Provides:      gem(openssl) = 3.1.0


%description
OpenSSL provides SSL, TLS and general purpose cryptography. It wraps the OpenSSL
library.


%package       -n gem-openssl-doc
Version:       3.1.0
Release:       alt1
Summary:       It wraps the OpenSSL library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета openssl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(openssl) = 3.1.0

%description   -n gem-openssl-doc
It wraps the OpenSSL library documentation files.

%description   -n gem-openssl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета openssl.


%package       -n gem-openssl-devel
Version:       3.1.0
Release:       alt1
Summary:       It wraps the OpenSSL library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета openssl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(openssl) = 3.1.0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 3.0

%description   -n gem-openssl-devel
It wraps the OpenSSL library development package.

%description   -n gem-openssl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета openssl.


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
%ruby_gemextdir

%files         -n gem-openssl-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-openssl-devel
%doc README.md
%ruby_includedir/*


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.0[1] -> 3.1.0

* Wed Jul 06 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.0.1-alt0.1
- ^ 2.2.0 -> 3.0.0[1]

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with usage Ruby Policy 2.0

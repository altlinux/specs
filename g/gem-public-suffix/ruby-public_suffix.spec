%define        gemname public_suffix

Name:          gem-public-suffix
Version:       4.0.6
Release:       alt1
Summary:       Domain name parser for Ruby based on the Public Suffix List
License:       MIT
Group:         Development/Ruby
Url:           https://simonecarletti.com/code/publicsuffix-ruby/
Vcs:           https://github.com/weppos/publicsuffix-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names public_suffix,public-suffix
Obsoletes:     ruby-public_suffix < %EVR
Provides:      ruby-public_suffix = %EVR
Provides:      gem(public_suffix) = 4.0.6


%description
PublicSuffix can parse and decompose a domain name into top level domain, domain
and subdomains.


%package       -n gem-public-suffix-doc
Version:       4.0.6
Release:       alt1
Summary:       Domain name parser for Ruby based on the Public Suffix List documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета public_suffix
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(public_suffix) >= 4.0.3 gem(public_suffix) < 5

%description   -n gem-public-suffix-doc
Domain name parser for Ruby based on the Public Suffix List documentation
files.

PublicSuffix can parse and decompose a domain name into top level domain, domain
and subdomains.

%description   -n gem-public-suffix-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета public_suffix.


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

%files         -n gem-public-suffix-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.6-alt1
- ^ 4.0.3 -> 4.0.6

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.3-alt1
- updated (^) 4.0.1 -> 4.0.3
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.0.1-alt1
- updated (^) 3.0.3 -> 4.0.1
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- New version.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Thu Nov 09 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version

* Sun Aug 06 2017 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version

* Tue Jan 31 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- Initial build in Sisyphus

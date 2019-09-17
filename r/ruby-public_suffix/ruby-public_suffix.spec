%define        pkgname public_suffix

Name: 	       ruby-%pkgname
Version:       4.0.1
Release:       alt1
Summary:       Domain name parser for Ruby based on the Public Suffix List
License:       MIT
Group:         Development/Ruby
Url:           https://simonecarletti.com/code/publicsuffix-ruby/
%vcs           https://github.com/weppos/publicsuffix-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
PublicSuffix can parse and decompose a domain name into top level
domain, domain and subdomains.


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
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.0.1-alt1
- ^ v4.0.1
- ^ Ruby Policy 2.0

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

%define        pkgname azure

Name: 	       ruby-%pkgname
Version:       0.7.10
Release:       alt3.1
Summary:       Microsoft Azure Client Library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/azure/azure-sdk-for-ruby
Vcs:           https://github.com/Azure/azure-sdk-for-ruby.git#asm
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%gem_replace_version thor ~> 1.0

%description
Official Ruby client library to consume Microsoft Azure services.


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
%_bindir/pfxer
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 0.7.10-alt3.1
- ! spec

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.10-alt3
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.10-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.10-alt2
- Disable tests.

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.10-alt1
- New version

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.9-alt1
- Initial build for ALT Linux

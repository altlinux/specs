%define        pkgname loofah

Name:          gem-%pkgname
Version:       2.4.0
Release:       alt1
Summary:       HTML/XML manipulation and sanitization based on Nokogiri
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flavorjones/loofah
Vcs:           https://github.com/flavorjones/loofah.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

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
%ruby_sitelibdir/*
%rubygem_specdir/*

%files         doc
%ruby_ri_sitedir/*


%changelog
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.2.3 -> 2.4.0

* Wed Mar 27 2019 Ivan A. Melnikov <iv@altlinux.org> 2.2.3-alt1
- 2.2.3 (CVE-2018-16468);
- fix version in gamespec for packaging (closes: #36441).

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.2-alt1
- Initial build for Sisyphus

%define        pkgname mini-mime
%define        gemname mini_mime

Name:          gem-%pkgname
Version:       1.0.2
Release:       alt1.1
Summary:       Minimal mime type library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/discourse/mini_mime
Vcs:           https://github.com/discourse/mini_mime.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname
Provides:      ruby-%gemname

%description
Minimal mime type implementation for use with the mail and rest-client gem.


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
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- updated (^) 1.0.1 -> 1.0.2
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- updated (^) 1.0.0 -> 1.0.1

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild dor new Ruby autorequirements.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

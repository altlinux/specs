%define        pkgname addressable

Name:          ruby-%pkgname
Version:       2.7.0
Release:       alt1
Summary:       Addressable is a replacement for the URI implementation that is part of Ruby's standard library
Summary(ru_RU.UTF-8): "Адресуемый" есть заменою воплощения URI, который является частью стандартной библиотеки рубина
Group:         Development/Ruby
License:       Apache-2.0
URL:           http://addressable.rubyforge.org/
# VCS:         https://github.com/sporkmonger/addressable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Addressable is a replacement for the URI implementation that is part of
Ruby's standard library. It more closely conforms to RFC 3986, RFC 3987,
and RFC 6570 (level 4), providing support for IRIs and URI templates.

%description   -l ru_RU.UTF-8
"Адресуемый" есть замена воплощения URI, который является частью стандартной
библиотеки рубина. Бн более точно удовлетворяет стандартам RFC 3986, RFC 3987,
и RFC 6570 (уровня 4), поддержиивая IRI и URI шаблоны.


%package       doc
Summary:       Documentation for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation for %{name}.

%description   -l ru_RU.UTF-8 doc
Документация для %{name}.


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
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- ^ v2.7.0
- ^ Ruby Policy 2.0

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- Bump to 2.6.0

* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt3
- Enable replace hardcoded path to "unicode.data" to ALT system's one.

* Mon Dec 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt2
- Fixed packing procedure of the "unicode.data" file
- Added russian translations to spec.

* Sun Aug 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Aug 25 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.2-alt1
- New version

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.1-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Sun Jun 05 2016 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Wed Mar 05 2014 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- Initial build for ALT Linux

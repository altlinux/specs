%define        gemname addressable

Name:          gem-addressable
Version:       2.8.0
Release:       alt1
Summary:       Addressable is a replacement for the URI implementation that is part of Ruby's standard library
Summary(ru_RU.UTF-8): "Адресуемый" есть заменою воплощения URI, который является частью стандартной библиотеки рубина
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/sporkmonger/addressable
Vcs:           https://github.com/sporkmonger/addressable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(public_suffix) >= 2.0.2 gem(public_suffix) < 5.0
BuildRequires: gem(bundler) >= 1.0 gem(bundler) < 3.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(public_suffix) >= 2.0.2 gem(public_suffix) < 5.0
Obsoletes:     ruby-addressable < %EVR
Provides:      ruby-addressable = %EVR
Provides:      gem(addressable) = 2.8.0


%description
Addressable is a replacement for the URI implementation that is part of Ruby's
standard library. It more closely conforms to RFC 3986, RFC 3987, and RFC 6570
(level 4), providing support for IRIs and URI templates.

%description         -l ru_RU.UTF-8
"Адресуемый" есть замена воплощения URI, который является частью стандартной
библиотеки рубина. Бн более точно удовлетворяет стандартам RFC 3986, RFC 3987, и
RFC 6570 (уровня 4), поддержиивая IRI и URI шаблоны.


%package       -n gem-addressable-doc
Version:       2.8.0
Release:       alt1
Summary:       Addressable is a replacement for the URI implementation that is part of Ruby's standard library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета addressable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(addressable) = 2.8.0

%description   -n gem-addressable-doc
Addressable is a replacement for the URI implementation that is part of Ruby's
standard library documentation files.

Addressable is a replacement for the URI implementation that is part of Ruby's
standard library. It more closely conforms to RFC 3986, RFC 3987, and RFC 6570
(level 4), providing support for IRIs and URI templates.

%description   -n gem-addressable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета addressable.


%package       -n gem-addressable-devel
Version:       2.8.0
Release:       alt1
Summary:       Addressable is a replacement for the URI implementation that is part of Ruby's standard library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета addressable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(addressable) = 2.8.0
Requires:      gem(bundler) >= 1.0 gem(bundler) < 3.0

%description   -n gem-addressable-devel
Addressable is a replacement for the URI implementation that is part of Ruby's
standard library development package.

Addressable is a replacement for the URI implementation that is part of Ruby's
standard library. It more closely conforms to RFC 3986, RFC 3987, and RFC 6570
(level 4), providing support for IRIs and URI templates.

%description   -n gem-addressable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета addressable.


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

%files         -n gem-addressable-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-addressable-devel
%doc README.md


%changelog
* Sun Jul 18 2021 Pavel Skrylev <majioa@altlinux.org> 2.8.0-alt1
- ^ 2.7.0 -> 2.8.0

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- updated (^) v2.7.0
- used (>) Ruby Policy 2.0

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

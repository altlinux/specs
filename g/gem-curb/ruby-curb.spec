%define        gemname curb

Name:          gem-curb
Version:       0.9.11
Release:       alt1
Summary:       Ruby bindings for libcurl
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/taf2/curb
Vcs:           https://github.com/taf2/curb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcurl-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bench
Obsoletes:     ruby-curb < %EVR
Provides:      ruby-curb = %EVR
Provides:      gem(curb) = 0.9.11


%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for the
libcurl(3), a fully-featured client-side URL transfer library. cURL and libcurl
live at http://curl.haxx.se/ .

Curb is a work-in-progress, and currently only supports libcurl's 'easy' and
'multi' modes.


%package       -n gem-curb-doc
Version:       0.9.11
Release:       alt1
Summary:       Ruby bindings for libcurl documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета curb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(curb) = 0.9.11

%description   -n gem-curb-doc
Ruby bindings for libcurl documentation files.

Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for the
libcurl(3), a fully-featured client-side URL transfer library. cURL and libcurl
live at http://curl.haxx.se/ .

Curb is a work-in-progress, and currently only supports libcurl's 'easy' and
'multi' modes.

%description   -n gem-curb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета curb.


%package       -n gem-curb-devel
Version:       0.9.11
Release:       alt1
Summary:       Ruby bindings for libcurl development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета curb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(curb) = 0.9.11

%description   -n gem-curb-devel
Ruby bindings for libcurl development package.

Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for the
libcurl(3), a fully-featured client-side URL transfer library. cURL and libcurl
live at http://curl.haxx.se/ .

Curb is a work-in-progress, and currently only supports libcurl's 'easy' and
'multi' modes.

%description   -n gem-curb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета curb.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-curb-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-curb-devel
%doc README.markdown
%ruby_includedir/*


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.11-alt1
- ^ 0.9.10 -> 0.9.11

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.10-alt1
- ^ 0.9.9 -> 0.9.10
- ! spec tags and syntax

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.9-alt1
- > Ruby Policy 2.0
- ^ 0.9.7 -> 0.9.9

* Wed Nov 07 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.7-alt1
- ^ 0.9.6 -> 0.9.7

* Fri Nov 02 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.6-alt1
- ^ 0.9.4 -> 0.9.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.6
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.5
- Rebuild for aarch64.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Leonid Krivoshein <klark@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

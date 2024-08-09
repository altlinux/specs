%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rdiscount

Name:          gem-rdiscount
Version:       2.2.7.3
Release:       alt1
Summary:       Discount (For Ruby) Implementation of John Gruber's Markdown
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://dafoster.net/projects/rdiscount/
Vcs:           https://github.com/davidfstr/rdiscount.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rdiscount) = 2.2.7.3


%description
Discount is an implementation of John Gruber's Markdown markup language in C. It
implements all of the language described in the markdown syntax document and
passes the Markdown 1.0 test suite.


%package       -n rdiscount
Version:       2.2.7.3
Release:       alt1
Summary:       Discount (For Ruby) Implementation of John Gruber's Markdown executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rdiscount
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rdiscount) = 2.2.7.3

%description   -n rdiscount
Discount (For Ruby) Implementation of John Gruber's Markdown
executable(s).

Discount is an implementation of John Gruber's Markdown markup language in C. It
implements all of the language described in the markdown syntax document and
passes the Markdown 1.0 test suite.

%description   -n rdiscount -l ru_RU.UTF-8
Исполнямка для самоцвета rdiscount.


%if_enabled    doc
%package       -n gem-rdiscount-doc
Version:       2.2.7.3
Release:       alt1
Summary:       Discount (For Ruby) Implementation of John Gruber's Markdown documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rdiscount
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rdiscount) = 2.2.7.3

%description   -n gem-rdiscount-doc
Discount (For Ruby) Implementation of John Gruber's Markdown documentation
files.

Discount is an implementation of John Gruber's Markdown markup language in C. It
implements all of the language described in the markdown syntax document and
passes the Markdown 1.0 test suite.

%description   -n gem-rdiscount-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rdiscount.
%endif


%if_enabled    devel
%package       -n gem-rdiscount-devel
Version:       2.2.7.3
Release:       alt1
Summary:       Discount (For Ruby) Implementation of John Gruber's Markdown development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rdiscount
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rdiscount) = 2.2.7.3
Conflicts:     libsexpr-devel
Conflicts:     libbobpp-devel
Conflicts:     libdiscount-devel
Conflicts:     libpicosat-devel

%description   -n gem-rdiscount-devel
Discount (For Ruby) Implementation of John Gruber's Markdown development
package.

Discount is an implementation of John Gruber's Markdown markup language in C. It
implements all of the language described in the markdown syntax document and
passes the Markdown 1.0 test suite.

%description   -n gem-rdiscount-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rdiscount.
%endif


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

%files         -n rdiscount
%doc README.markdown
%_bindir/rdiscount
%_mandir/markdown.7.xz
%_mandir/rdiscount.1.xz

%if_enabled    doc
%files         -n gem-rdiscount-doc
%doc README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rdiscount-devel
%doc README.markdown
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 2.2.7.3-alt1
- ^ 2.2.0.2 -> 2.2.7.3

* Mon Apr 04 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.0.2-alt1.1
- ! spec

* Tue Dec 22 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0.2-alt1
- ^ 2.2.0.1 -> 2.2.0.2
- ! spec

* Thu Jun 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4.6
- + conflict dep to libbobpp-devel, libdiscount-devel, libpicosat-devel

* Mon May 25 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4.5
- + conflict dep to libsexpr-devel

* Wed Apr 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4.4
- + proper buildarch for rdiscount package

* Fri Apr 03 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4.3
- * minor in build requires

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4.2
- fixed (!) spex

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4.1
- fixed (!) spec according to changelog rules

* Thu Jul 25 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt4
- fixed (!) spec
- added (+) ronn gem build dependency

* Wed Apr 10 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt3
- Clean up the spec from the dog-nail

* Tue Apr 09 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt2.1
- Fix build on i586 with a workaround dog-nail

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0.1-alt2
- Use Ruby Policy 2.0
- Fix spec

* Mon Sep 03 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0.1-alt1.2
- Rebuild for new Ruby autorequirements.

* Sat Jun 09 2018 Alexey Shabalin <shaba@altlinux.ru> 2.2.0.1-alt1.1
- NMU: rebuild for aarch64

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.0.1-alt1
- Initial build for Sisyphus

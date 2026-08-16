%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname plist

Name:          gem-plist
Version:       3.7.2
Release:       alt1
Summary:       All-purpose Property List manipulation library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bleything/plist
Vcs:           https://github.com/bleything/plist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(test-unit) >= 3.3.5
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Requires:      ruby >= 1.9.3
Requires:      gem(base64) >= 0
Obsoletes:     ruby-plist < %EVR
Provides:      ruby-plist = %EVR
Provides:      gem(plist) = 3.7.2

%description
Plist is a library to manipulate Property List files, also known as plists. It
can parse plist files into native Ruby data structures as well as generating new
plist files from your Ruby objects.


%if_enabled    doc
%package       -n gem-plist-doc
Version:       3.7.2
Release:       alt1
Summary:       All-purpose Property List manipulation library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета plist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(plist) = 3.7.2

%description   -n gem-plist-doc
All-purpose Property List manipulation library for Ruby documentation
files.

Plist is a library to manipulate Property List files, also known as plists. It
can parse plist files into native Ruby data structures as well as generating new
plist files from your Ruby objects.

%description   -n gem-plist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета plist.
%endif


%if_enabled    devel
%package       -n gem-plist-devel
Version:       3.7.2
Release:       alt1
Summary:       All-purpose Property List manipulation library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета plist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(plist) = 3.7.2
Requires:      gem(base64) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(test-unit) >= 3.3.5
Conflicts:     gem(rake) >= 14
Conflicts:     gem(test-unit) >= 4

%description   -n gem-plist-devel
All-purpose Property List manipulation library for Ruby development
package.

Plist is a library to manipulate Property List files, also known as plists. It
can parse plist files into native Ruby data structures as well as generating new
plist files from your Ruby objects.

%description   -n gem-plist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета plist.
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
%doc LICENSE.txt CHANGELOG.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-plist-doc
%doc LICENSE.txt CHANGELOG.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-plist-devel
%doc LICENSE.txt CHANGELOG.rdoc README.rdoc
%endif


%changelog
* Sun Aug 16 2026 Pavel Skrylev <majioa@altlinux.org> 3.7.2-alt1
- ^ 3.6.0 -> 3.7.2

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- ^ 3.4.0 -> 3.6.0

* Wed Jul 18 2018 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Return to Sisyphus

%define        gemname cap2

Name:          gem-cap2
Version:       0.2.2.1
Release:       alt0.1
Summary:       A Ruby library for managing Linux process and file capabilities
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lmars/cap2
Vcs:           https://github.com/lmars/cap2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libcap-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version cap2:0.2.2.1
Obsoletes:     ruby-cap2 < %EVR
Provides:      ruby-cap2 = %EVR
Provides:      gem(cap2) = 0.2.2.1


%description
Cap2 is a Ruby library for managing the POSIX 1003.1e capabilities available in
Linux kernels. These capabilities are a partitioning of the all powerful root
privilege into a set of distinct privileges. See capabilities(7) for more
information.


%package       -n gem-cap2-doc
Version:       0.2.2.1
Release:       alt0.1
Summary:       A Ruby library for managing Linux process and file capabilities documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cap2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cap2) = 0.2.2.1

%description   -n gem-cap2-doc
A Ruby library for managing Linux process and file capabilities documentation
files.

Cap2 is a Ruby library for managing the POSIX 1003.1e capabilities available in
Linux kernels. These capabilities are a partitioning of the all powerful root
privilege into a set of distinct privileges. See capabilities(7) for more
information.

%description   -n gem-cap2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cap2.


%package       -n gem-cap2-devel
Version:       0.2.2.1
Release:       alt0.1
Summary:       A Ruby library for managing Linux file and process capabilities development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cap2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cap2) = 0.2.2.1

%description   -n gem-cap2-devel
Cap2 is a Ruby library for managing the POSIX 1003.1e capabilities available in
Linux kernels.

These capabilities are a partitioning of the all powerful root privilege into a
set of distinct privileges.

See capabilites(7) for more information.


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
%ruby_gemextdir

%files         -n gem-cap2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-cap2-devel
%doc README.md


%changelog
* Fri Oct 08 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.2.1-alt0.1
- ^ 0.2.2 -> 0.2.2[.1]

* Tue Apr 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2.3
- ! spec's obsoletes/provides pair

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2.1
- fixed (!) spec according to changelog rules

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt2
- used (>) Ruby Policy 2.0
- fixed (!) spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1.1
- Rebuild for aarch64.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus

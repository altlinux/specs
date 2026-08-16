%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname net-ssh-multi

Name:          gem-net-ssh-multi
Version:       1.3.0
Release:       alt1
Summary:       Control multiple Net::SSH connections via a single interface
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/net-ssh/net-scp
Vcs:           https://github.com/net-ssh/net-scp.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(net-ssh) >= 2.6.5
BuildRequires: gem(net-ssh-gateway) >= 1.2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      rubygems > 1.3.1
Requires:      gem(net-ssh) >= 2.6.5
Requires:      gem(net-ssh-gateway) >= 1.2.0
Provides:      gem(net-ssh-multi) = 1.3.0

%description
Control multiple Net::SSH connections via a single interface.


%if_enabled    doc
%package       -n gem-net-ssh-multi-doc
Version:       1.3.0
Release:       alt1
Summary:       Control multiple Net::SSH connections via a single interface documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета net-ssh-multi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(net-ssh-multi) = 1.3.0

%description   -n gem-net-ssh-multi-doc
Control multiple Net::SSH connections via a single interface documentation
files.

%description   -n gem-net-ssh-multi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета net-ssh-multi.
%endif


%if_enabled    devel
%package       -n gem-net-ssh-multi-devel
Version:       1.3.0
Release:       alt1
Summary:       Control multiple Net::SSH connections via a single interface development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета net-ssh-multi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(net-ssh-multi) = 1.3.0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0

%description   -n gem-net-ssh-multi-devel
Control multiple Net::SSH connections via a single interface development
package.

%description   -n gem-net-ssh-multi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета net-ssh-multi.
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
%doc LICENSE.txt README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-net-ssh-multi-doc
%doc LICENSE.txt README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-net-ssh-multi-devel
%doc LICENSE.txt README.rdoc
%endif


%changelog
* Sun Aug 16 2026 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.3.0.pre1 -> 1.3.0
- * rebased to upstream git base
- * define explicit dependencies

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt0.1
- ^ 1.2.1 -> 1.3.0.pre1
- ! spec tags

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- Bump to 1.2.1
- Use Ruby Policy 2.0

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.4
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Thu Jul 05 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.2.0-alt1.3
- Tests disabled because is need an build for mipsel

* Wed Jul 04 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.2.0-alt1.2
- Add BuildRequires for mipsel

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- Initial build for ALT Linux

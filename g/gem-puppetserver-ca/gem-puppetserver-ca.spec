%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puppetserver-ca

Name:          gem-puppetserver-ca
Version:       2.7.0.1
Release:       alt0.1
Summary:       A simple Ruby CLI tool to interact with the Puppet Server's included CA
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppetserver-ca-cli
Vcs:           https://github.com/puppetlabs/puppetserver-ca-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(facter) >= 2.0.1
BuildRequires: gem(hocon) >= 1.2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(facter) >= 5
BuildConflicts: gem(hocon) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(facter) >= 2.0.1
Conflicts:     gem(facter) >= 5
Obsoletes:     ruby-puppetserver-ca-cli < %EVR
Provides:      ruby-puppetserver-ca-cli = %EVR
Provides:      gem(puppetserver-ca) = 2.7.0.1

%ruby_use_gem_version puppetserver-ca:2.7.0.1

%description
This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.


%package       -n puppetserver-ca
Version:       2.7.0.1
Release:       alt0.1
Summary:       A simple Ruby CLI tool to interact with the Puppet Server's included CA executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puppetserver-ca
Group:         Other
BuildArch:     noarch

Requires:      gem(puppetserver-ca) = 2.7.0.1

%description   -n puppetserver-ca
A simple Ruby CLI tool to interact with the Puppet Server's included CA
executable(s).

This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.

%description   -n puppetserver-ca -l ru_RU.UTF-8
Исполнямка для самоцвета puppetserver-ca.


%if_enabled    doc
%package       -n gem-puppetserver-ca-doc
Version:       2.7.0.1
Release:       alt0.1
Summary:       A simple Ruby CLI tool to interact with the Puppet Server's included CA documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppetserver-ca
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppetserver-ca) = 2.7.0.1
Obsoletes:     ruby-puppetserver-ca-cli-doc < %EVR
Provides:      ruby-puppetserver-ca-cli-doc = %EVR

%description   -n gem-puppetserver-ca-doc
A simple Ruby CLI tool to interact with the Puppet Server's included CA
documentation files.

This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.

%description   -n gem-puppetserver-ca-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppetserver-ca.
%endif


%if_enabled    devel
%package       -n gem-puppetserver-ca-devel
Version:       2.7.0.1
Release:       alt0.1
Summary:       A simple Ruby CLI tool to interact with the Puppet Server's included CA development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppetserver-ca
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppetserver-ca) = 2.7.0.1
Requires:      gem(bundler) >= 1.16
Requires:      gem(hocon) >= 1.2
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.4
Conflicts:     gem(hocon) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-puppetserver-ca-devel
A simple Ruby CLI tool to interact with the Puppet Server's included CA
development package.

This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.

%description   -n gem-puppetserver-ca-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppetserver-ca.
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
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n puppetserver-ca
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%_bindir/puppetserver-ca

%if_enabled    doc
%files         -n gem-puppetserver-ca-doc
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puppetserver-ca-devel
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Wed Mar 26 2025 Pavel Skrylev <majioa@altlinux.org> 2.7.0.1-alt0.1
- ^ 2.7.0 -> 2.7.0.1
- + automatic detection of current pupper/server config folder

* Fri Feb 14 2025 Pavel Skrylev <majioa@altlinux.org> 2.7.0-alt1
- ^ 2.4.0 -> 2.7.0

* Thu Mar 02 2023 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 1.7.0 -> 2.4.0

* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 1.4.0 -> 1.7.0
- ! spec tags
- ! pupper server paths in sources

* Tue Aug 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2
- > Ruby Policy 2.0

* Mon Aug 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt1
- Version updated to 1.4.0

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt2
- ca and puppet paths fixed

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt1
- Version updated to 1.3.1

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt1
- Version updated to 1.2.1

* Thu Dec 06 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus

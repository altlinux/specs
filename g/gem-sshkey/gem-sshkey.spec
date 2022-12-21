%define        gemname sshkey

Name:          gem-sshkey
Version:       2.0.0
Release:       alt1
Summary:       SSH private and public key generator in pure Ruby (RSA & DSA)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bensie/sshkey
Vcs:           https://github.com/bensie/sshkey.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR
Provides:      gem(sshkey) = 2.0.0


%description
SSH private and public key generator in pure Ruby (RSA & DSA).


%package       -n gem-sshkey-doc
Version:       2.0.0
Release:       alt1
Summary:       SSH private and public key generator in pure Ruby (RSA & DSA) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sshkey
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sshkey) = 2.0.0

%description   -n gem-sshkey-doc
SSH private and public key generator in pure Ruby (RSA & DSA) documentation
files.

%description   -n gem-sshkey-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sshkey.


%package       -n gem-sshkey-devel
Version:       2.0.0
Release:       alt1
Summary:       SSH private and public key generator in pure Ruby (RSA & DSA) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sshkey
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sshkey) = 2.0.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-sshkey-devel
SSH private and public key generator in pure Ruby (RSA & DSA) development
package.

%description   -n gem-sshkey-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sshkey.


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

%files         -n gem-sshkey-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sshkey-devel
%doc README.md


%changelog
* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.9.0 -> 2.0.0

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.0-alt1
- Initial build for Sisyphus

%define        gemname mixlib-shellout

Name:          gem-mixlib-shellout
Version:       3.2.5
Release:       alt1
Summary:       mixin library for subprocess management, output collection
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-shellout
Vcs:           https://github.com/chef/mixlib-shellout.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(chef-utils) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(chef-utils) >= 0
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR
Provides:      gem(mixlib-shellout) = 3.2.5


%description
Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.


%package       -n gem-mixlib-shellout-doc
Version:       3.2.5
Release:       alt1
Summary:       mixin library for subprocess management, output collection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-shellout
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mixlib-shellout) = 3.2.5

%description   -n gem-mixlib-shellout-doc
mixin library for subprocess management, output collection documentation
files.

Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.

%description   -n gem-mixlib-shellout-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-shellout.


%package       -n gem-mixlib-shellout-devel
Version:       3.2.5
Release:       alt1
Summary:       mixin library for subprocess management, output collection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mixlib-shellout
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mixlib-shellout) = 3.2.5

%description   -n gem-mixlib-shellout-devel
mixin library for subprocess management, output collection development
package.

Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.

%description   -n gem-mixlib-shellout-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mixlib-shellout.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-mixlib-shellout-doc
%ruby_gemdocdir

%files         -n gem-mixlib-shellout-devel


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.5-alt1
- ^ 3.1.4 -> 3.2.5

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.4-alt1
- ^ 3.0.11 -> 3.1.4

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.11-alt1
- > Ruby Policy 2.0
- ^ 2.4.0 -> 3.0.11

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux

%define        gemname ruby-libvirt

Name:          gem-ruby-libvirt
Version:       0.8.0
Release:       alt1.1
Summary:       Ruby bindings for libvirt
License:       LGPL-2.1-or-later
Group:         Development/Ruby
Url:           http://libvirt.org/ruby/
Vcs:           git://libvirt.org/ruby-libvirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libvirt-devel >= 0.4.0
BuildRequires: libruby-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-libvirt < %EVR
Obsoletes:     gem-libvirt < %EVR
Provides:      ruby-libvirt = %EVR
Provides:      gem-libvirt = %EVR
Provides:      gem(ruby-libvirt) = 0.8.0


%description
The module Libvirt provides bindings to libvirt.


%package       -n gem-ruby-libvirt-doc
Version:       0.8.0
Release:       alt1.1
Summary:       Ruby bindings for libvirt documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-libvirt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-libvirt) = 0.8.0
Obsoletes:     ruby-ruby-libvirt-doc
Provides:      ruby-ruby-libvirt-doc

%description   -n gem-ruby-libvirt-doc
Ruby bindings for libvirt documentation files.

The module Libvirt provides bindings to libvirt.

%description   -n gem-ruby-libvirt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-libvirt.


%package       -n gem-ruby-libvirt-devel
Version:       0.8.0
Release:       alt1.1
Summary:       Ruby bindings for libvirt development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-libvirt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-libvirt) = 0.8.0
Requires:      libvirt-devel >= 0.4.0
Requires:      libruby-devel

%description   -n gem-ruby-libvirt-devel
Ruby bindings for libvirt development package.

The module Libvirt provides bindings to libvirt.

%description   -n gem-ruby-libvirt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-libvirt.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README README.rdoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-ruby-libvirt-doc
%doc README README.rdoc
%ruby_gemdocdir

%files         -n gem-ruby-libvirt-devel
%doc README README.rdoc
%ruby_includedir/*


%changelog
* Thu Sep 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1.1
- ! add lost dep for devel package

* Tue Mar 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.7.1 -> 0.8.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt2.1
- ! spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt2
- > Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1.2
- Rebuild for new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
Initial build for Sisyphus.

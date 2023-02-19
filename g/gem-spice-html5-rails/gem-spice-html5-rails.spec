%define        gemname spice-html5-rails

Name:          gem-spice-html5-rails
Version:       0.1.5
Release:       alt1.2
Summary:       Spice HTML5 client packed for Rails application
License:       LGPLv3
Group:         Development/Ruby
Url:           https://www.spice-space.org/
Vcs:           https://github.com/abenari/spice-html5-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(railties) >= 3.1.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 3.1.0
Provides:      gem(spice-html5-rails) = 0.1.5


%description
The SPICE project aims to provide a complete open source solution for remote
access to virtual machines in a seamless way so you can play videos, record
audio, share usb devices and share folders without complications.

SPICE could be divided into 4 different components: Protocol, Client, Server and
Guest. The protocol is the specification in the communication of the three other
components; A client such as remote-viewer is responsible to send data and
translate the data from the Virtual Machine (VM) so you can interact with it;
The SPICE server is the library used by the hypervisor in order to share the VM
under SPICE protocol; And finally, the Guest side is all the software that must
be running in the VM in order to make SPICE fully functional, such as the QXL
driver and SPICE VDAgent.


%package       -n gem-spice-html5-rails-doc
Version:       0.1.5
Release:       alt1.2
Summary:       Spice HTML5 client packed for Rails application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spice-html5-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(spice-html5-rails) = 0.1.5

%description   -n gem-spice-html5-rails-doc
Spice HTML5 client packed for Rails application documentation files.

The SPICE project aims to provide a complete open source solution for remote
access to virtual machines in a seamless way so you can play videos, record
audio, share usb devices and share folders without complications.

SPICE could be divided into 4 different components: Protocol, Client, Server and
Guest. The protocol is the specification in the communication of the three other
components; A client such as remote-viewer is responsible to send data and
translate the data from the Virtual Machine (VM) so you can interact with it;
The SPICE server is the library used by the hypervisor in order to share the VM
under SPICE protocol; And finally, the Guest side is all the software that must
be running in the VM in order to make SPICE fully functional, such as the QXL
driver and SPICE VDAgent.

%description   -n gem-spice-html5-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spice-html5-rails.


%package       -n gem-spice-html5-rails-devel
Version:       0.1.5
Release:       alt1.2
Summary:       Spice HTML5 client packed for Rails application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spice-html5-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(spice-html5-rails) = 0.1.5

%description   -n gem-spice-html5-rails-devel
Spice HTML5 client packed for Rails application development package.

The SPICE project aims to provide a complete open source solution for remote
access to virtual machines in a seamless way so you can play videos, record
audio, share usb devices and share folders without complications.

SPICE could be divided into 4 different components: Protocol, Client, Server and
Guest. The protocol is the specification in the communication of the three other
components; A client such as remote-viewer is responsible to send data and
translate the data from the Virtual Machine (VM) so you can interact with it;
The SPICE server is the library used by the hypervisor in order to share the VM
under SPICE protocol; And finally, the Guest side is all the software that must
be running in the VM in order to make SPICE fully functional, such as the QXL
driver and SPICE VDAgent.

%description   -n gem-spice-html5-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spice-html5-rails.


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

%files         -n gem-spice-html5-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-spice-html5-rails-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1.2
- ! closes build dep under check condition

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1.1
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

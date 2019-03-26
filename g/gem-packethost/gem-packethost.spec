%define        pkgname packethost

Name:          gem-%pkgname
Version:       0.0.8
Release:       alt1
Summary:       A Ruby client for the Packet API
License:       GPLv2
Group:         Development/Ruby
Url:           https://www.packet.net
# VCS:         https://github.com/packethost/packet-rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Source:        %name-%version.tar
BuildArch:     noarch

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
%gem_replace_version activesupport ~> 5.0

%description
A Ruby client for the Packet API.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

%define        pkgname ovirt-engine-sdk

Name:          ruby-ovirt-engine-sdk
Version:       4.3.0
Release:       alt1
Summary:       The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/oVirt/ovirt-engine-sdk-ruby
# VCS:         https://github.com/oVirt/ovirt-engine-sdk-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: xmllint
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rubocop)
BuildRequires: gem(yard)
BuildRequires: gem(rspec-core)

%description
%summary.

This is a mirror from gerrit.ovirt.org http://www.ovirt.org, for issues use http://bugzilla.redhat.com


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch
Provides:      ruby-%pkgname-ruby-doc
Obsoletes:     ruby-%pkgname-ruby-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%package       -n gem-%pkgname-devel
Summary:       Development files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-devel
Development files for %gemname gem.


%prep
%setup
# create version.rb
echo "module OvirtSDK4;VERSION = '$(xmllint pom.xml --xpath "/*[name()='project']/*[name()='version']/text()")';end" > sdk/lib/ovirtsdk4/version.rb

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
- Use Ruby Policy 2.0
- Bump to 4.3.0

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- Initial build for Sisyphus

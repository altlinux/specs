%define        pkgname rubyntlm

Name:          gem-%pkgname
Version:       0.6.2
Release:       alt1
Summary:       Ruby/NTLM provides message creator and parser for the NTLM authentication
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/winrb/rubyntlm
# VCS:         https://github.com/WinRb/rubyntlm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

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

%files doc
%ruby_gemdocdir

%changelog
* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0

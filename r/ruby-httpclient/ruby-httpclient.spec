%define        pkgname httpclient

Summary:       HTTP accessing library for Ruby
Name:          ruby-%pkgname
Version:       2.8.3
Release:       alt1
Group:         Development/Ruby
License:       Ruby
Url:           https://github.com/nahi/httpclient
# VCS:         https://github.com/nahi/httpclient.git
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
HTTP library gives something like the functionality of libwww-perl (LWP) in Ruby


%package       doc
Summary:       Documentation for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation for %name

%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%_bindir/*
%ruby_gemlibdir
%ruby_gemspec

%files doc
%ruby_gemdocdir

%changelog
* Fri Feb 22 2019 Pavel Skrylev <majioa@altlinux.org> 2.8.3-alt1
- Bump to 2.8.3;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.2.4-alt1.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.2.4-alt1.1
- Rebuild with Ruby 2.4.1

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 2.8.2.4-alt1
- Update to latest release
 + Security CVE-2014-3566 critical to rhc:
   https://blog.openshift.com/poodle-ssl-vulnerability/

* Mon Aug 12 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.3.4.1-alt1
- Initial build for Sisyphus


%define        pkgname httpclient

Name:          gem-%pkgname
Version:       2.8.3.1
Release:       alt0.1
Summary:       HTTP accessing library for Ruby
Group:         Development/Ruby
License:       Ruby
Url:           https://github.com/nahi/httpclient
Vcs:           https://github.com/nahi/httpclient.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
HTTP library gives something like the functionality of libwww-perl (LWP) in Ruby


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%_bindir/*
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir


%changelog
* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.8.3.1-alt0.1
- ^ 2.8.3 -> 2.8.3.1pre
- ! spec tags

* Fri Feb 22 2019 Pavel Skrylev <majioa@altlinux.org> 2.8.3-alt1
- ^ 2.8.2.4 -> 2.8.3
- > Ruby Policy 2.0

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


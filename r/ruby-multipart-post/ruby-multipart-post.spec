%define        pkgname multipart-post

Name: 	       ruby-%pkgname
Version:       2.1.1
Release:       alt1
Summary:       Adds multipart POST capability to net/http
License:       None
Group:         Development/Ruby
Url:           https://github.com/nicksieger/multipart-post
%vcs           https://github.com/nicksieger/multipart-post.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Adds a streamy multipart form post capability to Net::HTTP. Also supports other
methods besides POST.


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
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ v2.1.1
- ^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 2.0.0-alt1
- Initial build in Sisyphus

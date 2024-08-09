%define        gemname rbtree

Name:          gem-rbtree
Version:       0.4.4
Release:       alt2
Summary:       A sorted associative collection
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/majioa/rbtree
Vcs:           https://github.com/majioa/rbtree.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(rbtree) = 0.4.4


%description
A RBTree is a sorted associative collection that is implemented with a Red-Black
Tree. It maps keys to values like a Hash, but maintains its elements in
ascending key order. The interface is the almost identical to that of Hash.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir


%changelog
* Tue Jul 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.4-alt2
- patch rb_cData for novel ruby

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.4-alt1
- + packaged gem with Ruby Policy 2.0

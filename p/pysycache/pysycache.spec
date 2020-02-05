Name:       pysycache
Version:    3.1
Release:    alt3

Summary: Pysycache  - educational software to learn to manipulate the mouse with pleasant activities.
Summary(ru_RU.UTF-8): Pysycache - обучающая программа для детей, помогающая освоить манипулятор "мышь"

License:    GPLv2
Group:      Games/Educational
Url:        http://www.pysycache.org
Packager:   Andrey Cherepanov <cas@altlinux.org>

BuildArch:  noarch

Source:     %name-%version.tar.gz
Patch0:     port-to-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Requires: python3-module-opencv3.4


%description
Pysycache - educational software to learn to manipulate the mouse with
pleasant activities.
Project have been initially started by Vincent DEROO
Vincent DEROO <vincent.pysycache@free.fr>

%description -l ru_RU.UTF-8
Pysycache - обучающая программа для детей, помогающая освоить 
манипулятор "мышь". Проект был начат Винсентом Деру
Vincent DEROO <vincent.pysycache@free.fr>

%prep
%setup -q
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%install
# Copy all program files
mkdir -p %buildroot
cp -a usr %buildroot/

# Create default configuratiuon
mkdir -p %buildroot%_sysconfdir/%name/
cat >  %buildroot%_sysconfdir/%name/%name.dfg <<EOF
USER=0
SCORE=/var/lib/pysycache
REPUSER=/var/lib/pysycache/users
EOF

# Create work directories
for d in themes-buttons themes-click themes-dblclick themes-move themes-puzzle users; do 
    mkdir -p %buildroot%_var/lib/%name/$d/ 
done

%files
%_bindir/%name
%_sysconfdir/%name/%name.dfg
%_datadir/applications/*.desktop
%_man1dir/%name.1.*
%_datadir/%name/*
%_datadir/pixmaps/*
%_var/lib/%name/*


%changelog
* Wed Feb 05 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1-alt3
- Porting to python3.

* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 3.1-alt2
- Do not use strict extension for man pages

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1-alt1.1
- Rebuild with Python-2.7

* Wed Aug 17 2011 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- Initial build in Sisyphus (thanks YYY) (closes: #26073)


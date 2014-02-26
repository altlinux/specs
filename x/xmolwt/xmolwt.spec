Name: xmolwt
Version: 0.7
Release: alt1

Summary: Molecular Weight & Elemental Analysis Calculator
License: distributable
Group: Sciences/Chemistry

Url: http://www.st.hirosaki-u.ac.jp/~rmiya/xmolwt/xmolwt-e.html
Source: http://www.st.hirosaki-u.ac.jp/~rmiya/xmolwt/%name-%version.tar.gz

BuildRequires: gtk+-devel

%define _applnkdir %_datadir/applnk
%define desktop_cat Edutainment/Science

%description 
This program calculate formula weight and percent of each elements
for the given chemical formula.

%prep
%setup
sed -i "s/\`\$(GTKCONFIG) --libs\` \$(OBJS) -o \$\@/\$(OBJS) -o \$\@ \`\$(GTKCONFIG) --libs\`/g" Makefile.gtk

%build
make -f Makefile.gtk CFLAGS="-DGTK %optflags" GTKCONFIG=gtk-config

%install
install -pm755 -d %buildroot%_bindir
install -pm755 gmolwt %buildroot%_bindir
(cd %buildroot%_bindir; ln -s gmolwt molwt)

install -pm 755 -d %buildroot%_applnkdir/%desktop_cat
cat > %buildroot%_applnkdir/%desktop_cat/gmolwt.desktop <<EOF
[Desktop Entry]
Name=gmolwt
Comment=Molecular Weight Calculator
Categories=Applications;Sciences;Chemistry
Exec=gmolwt
Terminal=0
Type=Application
EOF

%files
%doc Readme Howtouse.jp dot.gtkrc
%doc xmolwt.html xmolwt-e.html gmolwt.gif xmolwt.gif
%_bindir/gmolwt
%_bindir/molwt
%_applnkdir/%desktop_cat/gmolwt.desktop

%changelog
* Wed Feb 26 2014 Michael Shigorin <mike@altlinux.org> 0.7-alt1
- rebuilt for Sisyphus, thanks ogion@

* Fri Feb 22 2010 Denis G. Samsonenko <d.g.samsonenko@gmail.com> 0.7-alt0.sdg1
- build for ALTLinux

* Fri Nov 30 2001 MIYAMOTO Ryo <rmiya@cc.hirosaki-u.ac.jp>
- revised to version 0.7, changing in count.c

* Wed Aug 22 2001 MIYAMOTO Ryo <rmiya@cc.hirosaki-u.ac.jp>
- revised to version 0.6

* Tue Mar 13 2001 KAWAMURA Masao <kawamura@mlb.co.jp>
- initial rpm release

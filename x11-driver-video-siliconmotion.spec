Name: x11-driver-video-siliconmotion
Version: 1.5.1
Release: %mkrel 2
Summary: The X.org driver for Silicon Motion Cards
Group: Development/X11

########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-siliconmotion  xorg/drivers/xf86-video-siliconmotion
# cd xorg/drivers/xf86-video/siliconmotion
# git-archive --format=tar --prefix=xf86-video-siliconmotion-1.5.1/ master | bzip2 -9 > xf86-video-siliconmotion-1.5.1.tar.bz2
########################################################################
Source0: xf86-video-siliconmotion-%{version}.tar.bz2

License: MIT

########################################################################
# git-format-patch master..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for Silicon Motion Cards


%prep
%setup -q -n xf86-video-siliconmotion-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/siliconmotion_drv.la
%{_libdir}/xorg/modules/drivers/siliconmotion_drv.so
%{_mandir}/man4/siliconmotion.*

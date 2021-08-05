import grid_common as gr
import params_common as par
import matplotlib.pyplot as plt
import numpy as np

first=True

drawrho=False
drawpres=False
drawvz=False
drawdot=False
drawwave=False

line1, line2, line3, fig1, fig2, fig3, ax1, ax2, ax3 =0, 0, 0, 0, 0, 0, 0, 0, 0
dot1, dot2, dot3 = 0, 0, 0
linean1, linean2, linean3 = 0, 0, 0
txt_it1, txt_t1, txt_it2, txt_t1, txt_it3, txt_t3 = 0, 0, 0, 0, 0, 0 
maxpos10, maxpos20, maxpos30 = 0, 0, 0

def plotrout(rho,pres,vz,time,it):
    
    global first, line1, line2, line3, fig1, fig2, fig3, ax1, ax2, ax3
    global dot1, dot2, dot3, linean1, linean2, linean3
    global txt_it1, txt_t1, txt_it2, txt_t2, txt_it3, txt_t3
    global maxpos10, maxpos20, maxpos30
    
    if drawpres:
        presgr=(pres-par.p00)/par.p00
    if drawrho:
        rhogr=(rho-par.rho00)/par.rho00
    if drawvz:
        vzgr=(vz-par.vz00)/par.cs00
    
    
    # ---------------------
    # FIRST TIME CALL -----
    # ---------------------
    
    if first:
        plt.ion()
        
        posxtxt=gr.z0+0.75*(gr.zf-gr.z0)
        
        if drawdot or drawwave:
            yy=np.cos(2.*np.pi/(gr.zf-gr.z0)*(gr.zz-gr.z0-par.cs00*time))
        
        if drawpres:
            minim1=np.min(presgr)
            maxim1=np.max(presgr)
            posytxt_it1=maxim1*1.35   
            posytxt_t1=maxim1*1.20               
            fig1=plt.figure()
            ax1=fig1.add_subplot(111)
            ax1.axhline(y=0., c='black')
            ax1.axvline(x=(gr.zf+gr.z0)/2., c='black')
            ax1.axhline(y=maxim1, c='black',ls=':')
            ax1.axhline(y=minim1, c='black',ls=':')
            ax1.axvline(x=gr.z0, c='black',ls=':')
            ax1.axvline(x=gr.zf, c='black',ls=':')          
            line1,=ax1.plot(gr.zz,presgr,'r-')
            fig1.suptitle('(p-p00)/p00')
            txt_it1=ax1.text(posxtxt, posytxt_it1, 'it = '+str(it))
            txt_t1=ax1.text(posxtxt, posytxt_t1, 't = '+str(round(time,3)))
            plt.ylim([minim1*1.25,maxim1*1.75])
            plt.xlim([gr.z0-0.5,gr.zf+0.5])
            if drawdot:
                maxpos10=gr.zz[ np.where(presgr==maxim1)[0][0] ]
                dot1,=ax1.plot([maxpos10],[maxim1], marker='*', ls='', color='black')
            if drawwave:
                linean1,=ax1.plot( gr.zz, par.gam*par.amp*yy, ls='--', color='black')     
            fig1.canvas.draw()
            
        if drawrho:
            minim2=np.min(rhogr)
            maxim2=np.max(rhogr)  
            posytxt_it2=maxim2*1.35
            posytxt_t2=maxim2*1.20         
            fig2=plt.figure()
            ax2=fig2.add_subplot(111)
            ax2.axhline(y=0., c='black')
            ax2.axvline(x=(gr.zf+gr.z0)/2., c='black')        
            ax2.axhline(y=maxim2, c='black',ls=':')
            ax2.axhline(y=minim2, c='black',ls=':')
            ax2.axvline(x=gr.z0, c='black',ls=':')
            ax2.axvline(x=gr.zf, c='black',ls=':')                 
            line2,=ax2.plot(gr.zz,rhogr,'b-')
            fig2.suptitle('(rho-rho00)/rho00')
            txt_it2=ax2.text(posxtxt, posytxt_it2, 'it = '+str(it))
            txt_t2=ax2.text(posxtxt, posytxt_t2, 't = '+str(round(time,3)))        
            plt.ylim([minim2*1.25,maxim2*1.75])
            plt.xlim([gr.z0-0.5,gr.zf+0.5])
            if drawdot:
                maxpos20=gr.zz[ np.where(rhogr==maxim2)[0][0] ]
                dot2,=ax2.plot([maxpos20],[maxim2], marker='*', ls='', color='black')
            if drawwave:
                linean2,=ax2.plot( gr.zz, par.amp*yy, ls='--', color='black')
            fig2.canvas.draw()       
        
        if drawvz:
            minim3=np.min(vzgr)
            maxim3=np.max(vzgr)
            posytxt_it3=maxim3*1.35                 
            posytxt_t3=maxim3*1.20         
            fig3=plt.figure()
            ax3=fig3.add_subplot(111)
            ax3.axhline(y=0., c='black')
            ax3.axvline(x=(gr.zf+gr.z0)/2., c='black')        
            ax3.axhline(y=maxim3, c='black',ls=':')
            ax3.axhline(y=minim3, c='black',ls=':')
            ax3.axvline(x=gr.z0, c='black',ls=':')
            ax3.axvline(x=gr.zf, c='black',ls=':')                  
            line3,=ax3.plot(gr.zz,vzgr,'g-')
            fig3.suptitle('(vz-vz00)/cs00')    
            txt_it3=ax3.text(posxtxt, posytxt_it3, 'it = '+str(it))
            txt_t3=ax3.text(posxtxt, posytxt_t3, 't = '+str(round(time,3)))             
            plt.ylim([minim3*1.25,maxim3*1.75])
            plt.xlim([gr.z0-0.5,gr.zf+0.5])
            if drawdot:
                maxpos30=gr.zz[ np.where(vzgr==maxim3)[0][0] ]
                dot3,=ax3.plot([maxpos30],[maxim3], marker='*', ls='', color='black')
            if drawwave:
                linean3,=ax3.plot( gr.zz, par.amp*yy, ls='--', color='black')
            fig3.canvas.draw()

        first=False
        
    # ---------------------
    # FIRST TIME CALL - END
    # ---------------------
    
      
    # -- Wave propagating at cs00:
    # ----------------------------
    if drawwave:
        yy=np.cos(2.*np.pi/(gr.zf-gr.z0)*(gr.zz-gr.z0-par.cs00*time))

    # Update graphs:
    # --------------
            
    if drawpres:
        # UPDATE SOLUTION DATA
        line1.set_ydata((pres-par.p00)/par.p00)
        # UPDATE TEXT
        txt_it1.set_text('it = '+str(it))
        txt_t1.set_text('t = '+str(round(time,3)))
        # Draw sine sound wave?
        if drawwave:
            linean1.set_ydata( par.gam*par.amp*yy )
        # Draw moving dot?
        if drawdot:
            maxpos1=maxpos10+par.cs00*time+par.vz00*time
            if maxpos1>gr.zf:
                maxpos1=maxpos10+((maxpos1-gr.z0)/(gr.zf-gr.z0) - np.floor((maxpos1-gr.z0)/(gr.zf-gr.z0)) )*(gr.zf-gr.z0)
            dot1.set_xdata(maxpos1)
        # UPDATE CANVAS    
        fig1.canvas.draw()        
   
   
    if drawrho:
        # UPDATE SOLUTION DATA
        line2.set_ydata((rho-par.rho00)/par.rho00)
        # UPDATE TEXT
        txt_it2.set_text('it = '+str(it))
        txt_t2.set_text('t = '+str(round(time,3)))
        # Draw sine sound wave?
        if drawwave:
            linean2.set_ydata( par.amp*yy )    
        # Draw moving dot?
        if drawdot:
            maxpos2=maxpos20+par.cs00*time+par.vz00*time
            if maxpos2>gr.zf:
                maxpos2=maxpos20+((maxpos2-gr.z0)/(gr.zf-gr.z0) - np.floor((maxpos2-gr.z0)/(gr.zf-gr.z0)) )*(gr.zf-gr.z0)
            dot2.set_xdata(maxpos2)
        # UPDATE CANVAS   
        fig2.canvas.draw()
            
      
    if drawvz:
        # UPDATE SOLUTION DATA
        line3.set_ydata((vz-par.vz00)/par.cs00)
        # UPDATE TEXT
        txt_it3.set_text('it = '+str(it))
        txt_t3.set_text('t = '+str(round(time,3)))
        # Draw sine sound wave?
        if drawwave:
            linean3.set_ydata( par.amp*yy )
        if drawdot:
            maxpos3=maxpos30+par.cs00*time+par.vz00*time
            if maxpos3>gr.zf:
                maxpos3=maxpos30+((maxpos3-gr.z0)/(gr.zf-gr.z0) - np.floor((maxpos3-gr.z0)/(gr.zf-gr.z0)) )*(gr.zf-gr.z0)
            dot3.set_xdata(maxpos3)
        # UPDATE CANVAS    
        fig3.canvas.draw()

    
    
    

